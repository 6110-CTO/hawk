# SPDX-FileCopyrightText: 2022 Carnegie Mellon University <satya-group@lists.andrew.cmu.edu>
#
# SPDX-License-Identifier: GPL-2.0-only

import json
import os
import glob
import time
import yaml
from pathlib import Path
from typing import Dict

import torch
from logzero import logger

import shlex
import subprocess

from hawk import M_ZFILL
from hawk.context.model_trainer_context import ModelTrainerContext
from hawk.core.model_trainer import ModelTrainerBase
from hawk.core.model import Model
from hawk.trainer.yolo import PYTHON_EXEC
from hawk.trainer.yolo.model import YOLOModel
from hawk.core.utils import log_exceptions

torch.multiprocessing.set_sharing_strategy('file_system')


class YOLOTrainer(ModelTrainerBase):
    def __init__(self, context: ModelTrainerContext, args: Dict[str, str]):
        super().__init__(args)
        
        self.args['test_dir'] = self.args.get('test_dir', '')
        self.args['batch-size'] = int(self.args.get('batch-size', 16))
        self.args['image-size'] = int(self.args.get('image-size', 640))
        self.args['initial_model_epochs'] = int(self.args.get('initial_model_epochs', 30))
        self.train_initial_model = False 

        self.context = context

        self._model_dir = self.context.model_dir
        logger.info("Model_dir {}".format(self._model_dir))
        
        if self.args['test_dir']:
            self.test_dir = Path(self.args['test_dir'])
            msg = "Test Path {} provided does not exist".format(self.test_dir)
            assert self.test_dir.exists(), msg 
        
        if self.args['mode'] == "notional":
            assert "notional_model_path" in self.args, "Missing keyword {}".format("notional_model_path")
            notional_model_path = Path(self.args['notional_model_path'])
            msg = "Notional Model Path {} provided does not exist".format(notional_model_path)
            assert notional_model_path.exists(), msg

        logger.info("YOLO TRAINER CALLED")

    @log_exceptions
    def load_model(self, path:Path = "", content:bytes = b''):
        if isinstance(path, str):
            path = Path(path)

        if self.args['mode'] != "oracle":
            assert path.is_file() or len(content)
            new_version = self.get_new_version()
            if not path.is_file():
                path = self._model_dir / "model-{}.pt".format(str(new_version).zfill(M_ZFILL))  
                with open(path, "wb") as f:
                    f.write(content)     
            
        version = self.get_version()
        self.prev_path = path
        self.context.stop_model()
        logger.info(" Trainer Loading from path {}".format(path))
        return YOLOModel(self.args, path, version,  
                         mode=self.args['mode'],
                         context=self.context) 
  
    @log_exceptions
    def train_model(self, train_dir) -> Model:
        
        # check mode if not hawk return model
        # EXPERIMENTAL
        if self.args['mode'] == "oracle":
            return self.load_model(Path(""))
        elif self.args['mode'] == "notional":
            notional_path = self.args['notional_model_path']
            # sleep for training time
            time_sleep = self.args.get('notional_train_time', 0)
            time_now = time.time()
            while (time.time() - time_now) < time_sleep:
                time.sleep(1) 
                         
            return self.load_model(Path(notional_path))
             
        new_version = self.get_new_version()

        model_savepath = self._model_dir / "model-{}.pt".format(str(new_version).zfill(M_ZFILL))        
        trainpath = self._model_dir / "train-{}.txt".format(str(new_version).zfill(M_ZFILL)) 
               
        labels = ['1']
        train_samples = {l:glob.glob(str(train_dir / l / '*')) for l in labels}
        train_len = {l:len(train_samples[l]) for l in labels}
        if train_len['1'] == 0:
            logger.error(train_len)
            logger.error([str(train_dir / l / '*') for l in labels])
            raise Exception


        with open(trainpath, 'w') as f:
            for l in labels:
                for path in train_samples[l]:
                    f.write("{}\n".format(path))
        
        noval = True                    
        if self.args['test_dir']:
            noval = False
            valpath = self._model_dir / "val-{}.txt".format(str(new_version).zfill(M_ZFILL)) 
            with open(valpath, 'w') as f:
                for path in glob.glob(self.args['test_dir']+"/*/*"):
                    f.write("{}\n".format(path))
            

        if new_version <= 0:
            self.train_initial_model = True
            num_epochs = self.args['initial_model_epochs']
        else:
            online_epochs = json.loads(self.args['online_epochs'])
            
            if isinstance(online_epochs, list):
                for epoch, pos in online_epochs:
                    pos = int(pos)
                    epoch = int(epoch)
                    if train_len['1'] >= pos:
                        num_epochs = epoch
                        break 
            else:
                num_epochs = int(online_epochs)
            
        file_path = os.path.dirname(os.path.abspath(__file__))
        
        data_dict = {
            'path': str(self._model_dir),
            'train': str(trainpath),
            'nc': 1,
            'names': ['positive']
            }
        
        if not noval:
            data_dict['val'] = valpath

        data_file = os.path.join(self._model_dir, 'data.yaml')
        with open(data_file, 'w') as outfile:
            yaml.dump(data_dict, outfile, default_flow_style=False)

        if self.train_initial_model:
            weights= "yolov5s.pt"
        else:
            weights= self.prev_path

        cmd = "{} {}/yolov5/train.py --savepath {} \
               --epochs {} --batch-size {} \
               --weights {} --imgsz {} --data {}".format(
                  PYTHON_EXEC,
                  file_path,
                  model_savepath,
                  num_epochs,
                  self.args['batch-size'],
                  weights,
                  self.args['image-size'],
                  data_file
               )
        
        if self.args['test_dir']:
            cmd += " --noval False"

        logger.info("TRAIN CMD \n {}".format(cmd))
        proc = subprocess.Popen(shlex.split(cmd))
        proc.communicate()
        if not os.path.exists(model_savepath):
            raise FileNotFoundError
        logger.info("Training completed")

        
        self.prev_path = model_savepath

        model_args = self.args.copy()
        model_args['train_examples'] = train_len
        self.context.stop_model() 
        return YOLOModel(model_args, 
                         model_savepath,
                         new_version,
                         self.args['mode'], 
                         context=self.context) 
    