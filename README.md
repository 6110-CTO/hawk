<!--
SPDX-FileCopyrightText: 2022 Carnegie Mellon University <satya-group@lists.andrew.cmu.edu>

SPDX-License-Identifier: GPL-2.0-only
-->


# Hawk: Low-Bandwidth Remote Sensing of Rare Events

*Hawk* is a bandwidth-frugal learning system for discovering instances of rare
targets from weakly connected distributed data source called "scouts." The mission
starts with a machine learning (ML) model trained on very few labeled data.
The incoming data is inferred using the model. Hawk uses active learning techniques
to choose a small subset of data to query the labeler for annotations.
The obtained labels are added to the labeled training set to periodically improve the quality of
models present in the scouts.

More details about can be found [here.](/docs/README.md)

This is a developing project.

## Installation steps

### Step 0. Setting up Environment

If installing the system from scratch, first follow the wiki install instructions here:
[Install Instructions from Scratch](https://github.com/cmusatyalab/hawk/wiki/Hawk-from-Scratch)

### Step 1. Verify required artifacts
The standard Hawk mission requires a minimal set of artifacts.
- A dataset must be available on the scout.
- A booststrap dataset consisting of a small number of samples per class from the relvant dataset.  A .zip containing two directories 0/ and 1/, each containing positive and negative samples.
- An index file containing the full paths of each sample that will be stored on the scout for processing during a mission.  Example: [example_DOTA_stream_file](/configs/stream_example_DOTA_roundabout.txt)
- (Optional) An initial model trained on a small amount of data prior to the mission.

### Step 2. Modify mission configuration

Provide relevant data and model parameters in the [config file.](/configs/dota_sample_config.yml)  This config file is required to run a Hawk mission of any kind.  Currently, the mission configuration takes the form of a yaml file (.yml) but in the future a mission will be launched via the Flutter web gui.  The config file contains both administrative information (where data is located on a server) as well as more mission-focused parameters, such as the retraining policy, mode architecture to use, etc.  While most fields and subfields in the config file can be modified simply by changing a value, the specification of others require some small, additional administrative up front.

- mission-name: mission identifier
- train-location: scout or home (scout default)
- label-mode: script (ui is the other option when using the Flutter GUI).  Use script for functional testing and pure automation (no human interaction required).
- scouts: This field simply represents the list of server domain or IP addresses, e.g. scout1.mission.com, scout2.mission.com, etc.
- scout-params: This field contains a mission directory path on each scout which tell sthe scouts where to store log files and mission artifacts.
- home-params: the mission directory on home specifices where on the home station (from where the missino is launched) to aggregate and store mission logs from all scouts.
- dataset: This field contains information that tells Hawk how to read incoming data
    - type: random, tile, and a few others.  Because all tiles were derived from original, larger images, random simply treats all tiles as independent of each other, even if two were derived from the same image, and are thus assigned to scouts randomly.
    - stream_path: this is the path to the file (locally) that contains the entire list of image samples and associated labels to be read by the scouts.  Format is: <path/to/image.jpg> <label> An example stream file can be found here: [example_DOTA_stream_file](/configs/stream_example_DOTA_roundabout.txt) This file is used by `hawk_deploy split` in a later step.
    - index_path: this is the path to the file on each individual scout that is read by the respective scout.  Thus, each the file located at this location on each scout is unique from those on other scouts.
    - tiles_per_frame: By default, each scout inferences an entire image's worth of tiles in 20 seconds.  Therefore, this number determines how many total tiles are inferenced for every 20 seconds, to simply control the rate of inference by the scouts.
- retrain_policy: Logical conditions to determine when to retrain the existing model.
    - type: sepcifies the retraining mode (percentage, absolute)
    - only_positives: this flag specifies that only a certain increases positives affects retraining conditions, as opposed to positives and negatives.
    - threshold: percentage or absolute threshold for retrain conditions to be met.
- train_strategy: Specifies training and model details.
    - type: dnn_classifier, yolo, etc. the type of model used
    - initial_model_path: This allows the user to specify a path to an initial model on the home machine or on the scout.  If the path is invalid, a new model will be trained on the scouts at the beginning of the mission, otherwise the model pointed to by the specified path will be used.
    - bootstrap_path: This is the path to a .zip folder containing two directories: 0/ and 1/ where 1/ represents a directory of true positives (of the desired class) and 0/ represents the set of true negatives.  Common practice is to use 20 positives and 100 negatives, but any numbers can be used.  The bootstrap dataset is used to train the initial model if no valid path is given for intital_model_path.  The bootstrap dataset is also used for all future training iterations, so it is required.  An example list of images and labels that is used to generate this bootstrap dataset for initial training can be found here: [example_DOTA_train_file](/configs/train_example_DOTA_roundabout.txt)
    - args: additional arguments
        - mode: hawk / oracle / notional: hawk uses the inference score to prioritize (active learning) each sample for trasmission to home, oracle prioritizes each sample according to its ground truth label, and notional prioritizes according to its inference score, but does not iteratively retrain; uses a model pretrained on all data.
        - arch: model architecture - many choices to pick from
        - unfreeze_layers: the number of layers that are retrained each iteration, has various performance tradeoffs.
        - batch-size: inference batch-size on the scouts
        - online_epochs: training epochs for each subsequent training iteration
        - initial_model_epochs: number of training epochs for initial model if training on the scout from scratch
- selector: options for how samples are prioritized and selected for transmission.
    - type: topk, token, etc.  different methods select samples
    - topk (specific type arguments)
        - k: batch size per each transmission (4 samples transmitted)
        - batchSize: number of samples required to be inferenced before transmitting k samples to home.
- reexamination: options for how scouts reexamine samples inferenced in previous batches.
    - type: top, full, etc. - affects numbers of samples reexamined.
    - k: 100 - number of samples reexamined each time a new model is trained.
- bandwidth: scout-home bandwidth constraint (in kbps)

### Step 3. Split dataset across Scout Servers

The stream file on home provided in [config file.](/configs/dota_sample_config.yml), dataset: stream_path, contains a list of input images with associated labels.  The script below assumes the stream file contains all possible samples desired for inference during a mission, with the format:
<path/to/image1> <label_1>
<path/to/image2> <label_2>
...
where the labels are either 1 or 0 (pos or neg).  If using the DOTA dataset, all original images should be tiled to dimensions of 256x256, which can be done by referencing [DOTA Dev Kit](https://github.com/CAPTAIN-WHU/DOTA_devkit/tree/master).  This file thus points to data samples to be inferenced by the scouts.

The user can specify the index file (dataset: index_path) that will be generated from running `hawk_deploy split` below.
Run the following cmd to split the dataset across participating scouts
```bash
poetry run hawk_deploy split configs/dota_sample_config.yml
```
After running this script, the list of all samples from the stream file  will be approximately evenly split across the number of scouts defined in the config file.  These new per-scout index files will be stored on each respective scout at the location specified by dataset: index_path in the config file.

### Step 4. Start Hawk Mission from Home

```bash
poetry run hawk_home configs/config.yml
```
The configuration file will need to be modified to include the actual host name of the scout and will need to include the index file path location on the scout (see step 3).  If the mission successfully runs, you should see the scout retrieving and inferencing batches of images and periodically reporting scores of positives.


## Running Hawk UI
Hawk UI is developed using [Flutter SDK](https://docs.flutter.dev/get-started/install) and has been tested using Chrome browser.
The backend uses Flask REST API (Port:8000) to start and stop missions. The results are streamed to the front-end using websockets (Port:5000).

### Step 1. Setting up Environment
```bash
poetry install --extras home
```
### Step 2. ScopeCookie and Config

Assumes scope cookie (NEWSCOPE) and config file (config.yml) are present in ~/.hawk

```bash
mkdir -p ~/.hawk
cp ~/hawk/configs/flutter.yml ~/.hawk/config.yml
```
### Step 3. Start Home process
```bash
poetry run hawk_flutter
```

### Step 4. Start Flutter app
```bash
cd ~/hawk/hawk_ui
flutter run -d chrome
# if port forwarding use cmd below
# flutter run -d web-server --web-port=35415
```
Configure the filter using the UI and then click 'Start' to begin mission. The results can be viewed on 'Results' panel.

# Licensing

Unless otherwise stated, the source code is copyright Carnegie Mellon University and licensed under the GNU General Public License, version 2. Portions from the following third party sources have been modified and are included in this repository. These portions are noted in the source files and are copyrighted by their respective authors with the licenses listed.

Project | Modified | License
---|---|---|
[pytorch/examples](https://github.com/pytorch/examples) | Yes | BSD
[yolov5](https://github.com/ultralytics/yolov5) | Yes | GNUv3
