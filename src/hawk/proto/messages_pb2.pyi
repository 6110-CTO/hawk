"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    MessageMap as google___protobuf___internal___containers___MessageMap,
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
    ScalarMap as google___protobuf___internal___containers___ScalarMap,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

DatasetSplitValue = typing___NewType('DatasetSplitValue', builtin___int)
type___DatasetSplitValue = DatasetSplitValue
DatasetSplit: _DatasetSplit
class _DatasetSplit(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[DatasetSplitValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    TRAIN = typing___cast(DatasetSplitValue, 0)
    TEST = typing___cast(DatasetSplitValue, 1)
TRAIN = typing___cast(DatasetSplitValue, 0)
TEST = typing___cast(DatasetSplitValue, 1)

class MissionId(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    value: typing___Text = ...

    def __init__(self,
        *,
        value : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> None: ...
type___MissionId = MissionId

class ScoutConfiguration(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BandwidthFuncEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: builtin___int = ...
        value: typing___Text = ...

        def __init__(self,
            *,
            key : typing___Optional[builtin___int] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___BandwidthFuncEntry = BandwidthFuncEntry

    missionId: typing___Text = ...
    scouts: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    scoutIndex: builtin___int = ...
    homeIP: typing___Text = ...
    trainLocation: typing___Text = ...
    missionDirectory: typing___Text = ...
    bootstrapZip: builtin___bytes = ...
    validate: builtin___bool = ...
    class_list: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    novel_class_discovery: builtin___bool = ...
    sub_class_discovery: builtin___bool = ...

    @property
    def trainStrategy(self) -> type___TrainConfig: ...

    @property
    def retrainPolicy(self) -> type___RetrainPolicyConfig: ...

    @property
    def dataset(self) -> type___Dataset: ...

    @property
    def selector(self) -> type___SelectiveConfig: ...

    @property
    def reexamination(self) -> type___ReexaminationStrategyConfig: ...

    @property
    def initialModel(self) -> type___ModelArchive: ...

    @property
    def baseModel(self) -> type___ModelArchive: ...

    @property
    def bandwidthFunc(self) -> google___protobuf___internal___containers___ScalarMap[builtin___int, typing___Text]: ...

    @property
    def scml_deploy_opts(self) -> type___PerScoutSCMLOptions: ...

    def __init__(self,
        *,
        missionId : typing___Optional[typing___Text] = None,
        scouts : typing___Optional[typing___Iterable[typing___Text]] = None,
        scoutIndex : typing___Optional[builtin___int] = None,
        homeIP : typing___Optional[typing___Text] = None,
        trainLocation : typing___Optional[typing___Text] = None,
        missionDirectory : typing___Optional[typing___Text] = None,
        trainStrategy : typing___Optional[type___TrainConfig] = None,
        retrainPolicy : typing___Optional[type___RetrainPolicyConfig] = None,
        dataset : typing___Optional[type___Dataset] = None,
        selector : typing___Optional[type___SelectiveConfig] = None,
        reexamination : typing___Optional[type___ReexaminationStrategyConfig] = None,
        initialModel : typing___Optional[type___ModelArchive] = None,
        baseModel : typing___Optional[type___ModelArchive] = None,
        bootstrapZip : typing___Optional[builtin___bytes] = None,
        bandwidthFunc : typing___Optional[typing___Mapping[builtin___int, typing___Text]] = None,
        validate : typing___Optional[builtin___bool] = None,
        class_list : typing___Optional[typing___Iterable[typing___Text]] = None,
        scml_deploy_opts : typing___Optional[type___PerScoutSCMLOptions] = None,
        novel_class_discovery : typing___Optional[builtin___bool] = None,
        sub_class_discovery : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"baseModel",b"baseModel",u"dataset",b"dataset",u"initialModel",b"initialModel",u"reexamination",b"reexamination",u"retrainPolicy",b"retrainPolicy",u"scml_deploy_opts",b"scml_deploy_opts",u"selector",b"selector",u"trainStrategy",b"trainStrategy"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bandwidthFunc",b"bandwidthFunc",u"baseModel",b"baseModel",u"bootstrapZip",b"bootstrapZip",u"class_list",b"class_list",u"dataset",b"dataset",u"homeIP",b"homeIP",u"initialModel",b"initialModel",u"missionDirectory",b"missionDirectory",u"missionId",b"missionId",u"novel_class_discovery",b"novel_class_discovery",u"reexamination",b"reexamination",u"retrainPolicy",b"retrainPolicy",u"scml_deploy_opts",b"scml_deploy_opts",u"scoutIndex",b"scoutIndex",u"scouts",b"scouts",u"selector",b"selector",u"sub_class_discovery",b"sub_class_discovery",u"trainLocation",b"trainLocation",u"trainStrategy",b"trainStrategy",u"validate",b"validate"]) -> None: ...
type___ScoutConfiguration = ScoutConfiguration

class MissionStats(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OthersEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___OthersEntry = OthersEntry

    totalObjects: builtin___int = ...
    processedObjects: builtin___int = ...
    droppedObjects: builtin___int = ...
    falseNegatives: builtin___int = ...

    @property
    def others(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        totalObjects : typing___Optional[builtin___int] = None,
        processedObjects : typing___Optional[builtin___int] = None,
        droppedObjects : typing___Optional[builtin___int] = None,
        falseNegatives : typing___Optional[builtin___int] = None,
        others : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"droppedObjects",b"droppedObjects",u"falseNegatives",b"falseNegatives",u"others",b"others",u"processedObjects",b"processedObjects",u"totalObjects",b"totalObjects"]) -> None: ...
type___MissionStats = MissionStats

class TestResults(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    testExamples: builtin___int = ...
    auc: builtin___float = ...
    bestThreshold: builtin___float = ...
    precisions: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    recalls: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    version: builtin___int = ...

    @property
    def modelMetrics(self) -> type___ModelMetrics: ...

    def __init__(self,
        *,
        testExamples : typing___Optional[builtin___int] = None,
        auc : typing___Optional[builtin___float] = None,
        modelMetrics : typing___Optional[type___ModelMetrics] = None,
        bestThreshold : typing___Optional[builtin___float] = None,
        precisions : typing___Optional[typing___Iterable[builtin___float]] = None,
        recalls : typing___Optional[typing___Iterable[builtin___float]] = None,
        version : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"modelMetrics",b"modelMetrics"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"auc",b"auc",u"bestThreshold",b"bestThreshold",u"modelMetrics",b"modelMetrics",u"precisions",b"precisions",u"recalls",b"recalls",u"testExamples",b"testExamples",u"version",b"version"]) -> None: ...
type___TestResults = TestResults

class MissionResults(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ResultsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: builtin___int = ...

        @property
        def value(self) -> type___TestResults: ...

        def __init__(self,
            *,
            key : typing___Optional[builtin___int] = None,
            value : typing___Optional[type___TestResults] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ResultsEntry = ResultsEntry


    @property
    def results(self) -> google___protobuf___internal___containers___MessageMap[builtin___int, type___TestResults]: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Mapping[builtin___int, type___TestResults]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"results",b"results"]) -> None: ...
type___MissionResults = MissionResults

class ModelMetrics(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    truePositives: builtin___int = ...
    falsePositives: builtin___int = ...
    falseNegatives: builtin___int = ...
    precision: builtin___float = ...
    recall: builtin___float = ...
    f1Score: builtin___float = ...

    def __init__(self,
        *,
        truePositives : typing___Optional[builtin___int] = None,
        falsePositives : typing___Optional[builtin___int] = None,
        falseNegatives : typing___Optional[builtin___int] = None,
        precision : typing___Optional[builtin___float] = None,
        recall : typing___Optional[builtin___float] = None,
        f1Score : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"f1Score",b"f1Score",u"falseNegatives",b"falseNegatives",u"falsePositives",b"falsePositives",u"precision",b"precision",u"recall",b"recall",u"truePositives",b"truePositives"]) -> None: ...
type___ModelMetrics = ModelMetrics

class ImportModel(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    path: typing___Text = ...

    @property
    def model(self) -> type___ModelArchive: ...

    def __init__(self,
        *,
        model : typing___Optional[type___ModelArchive] = None,
        path : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"model",b"model"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"model",b"model",u"path",b"path"]) -> None: ...
type___ImportModel = ImportModel

class ModelArchive(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    content: builtin___bytes = ...
    version: builtin___int = ...

    def __init__(self,
        *,
        content : typing___Optional[builtin___bytes] = None,
        version : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content",u"version",b"version"]) -> None: ...
type___ModelArchive = ModelArchive

class TrainConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def dnn_classifier(self) -> type___ModelConfig: ...

    @property
    def yolo(self) -> type___ModelConfig: ...

    @property
    def fsl(self) -> type___ModelConfig: ...

    @property
    def dnn_classifier_radar(self) -> type___ModelConfig: ...

    @property
    def yolo_radar(self) -> type___ModelConfig: ...

    def __init__(self,
        *,
        dnn_classifier : typing___Optional[type___ModelConfig] = None,
        yolo : typing___Optional[type___ModelConfig] = None,
        fsl : typing___Optional[type___ModelConfig] = None,
        dnn_classifier_radar : typing___Optional[type___ModelConfig] = None,
        yolo_radar : typing___Optional[type___ModelConfig] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"dnn_classifier",b"dnn_classifier",u"dnn_classifier_radar",b"dnn_classifier_radar",u"fsl",b"fsl",u"value",b"value",u"yolo",b"yolo",u"yolo_radar",b"yolo_radar"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dnn_classifier",b"dnn_classifier",u"dnn_classifier_radar",b"dnn_classifier_radar",u"fsl",b"fsl",u"value",b"value",u"yolo",b"yolo",u"yolo_radar",b"yolo_radar"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["dnn_classifier","yolo","fsl","dnn_classifier_radar","yolo_radar"]: ...
type___TrainConfig = TrainConfig

class ModelConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ArgsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ArgsEntry = ArgsEntry


    @property
    def args(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        args : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"args",b"args"]) -> None: ...
type___ModelConfig = ModelConfig

class YOLOConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    imageSize: builtin___int = ...
    args: typing___Text = ...

    def __init__(self,
        *,
        imageSize : typing___Optional[builtin___int] = None,
        args : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"args",b"args",u"imageSize",b"imageSize"]) -> None: ...
type___YOLOConfig = YOLOConfig

class RetrainPolicyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def absolute(self) -> type___AbsolutePolicyConfig: ...

    @property
    def percentage(self) -> type___PercentagePolicyConfig: ...

    @property
    def model(self) -> type___ModelPolicyConfig: ...

    @property
    def sample(self) -> type___SampleIntervalPolicyConfig: ...

    def __init__(self,
        *,
        absolute : typing___Optional[type___AbsolutePolicyConfig] = None,
        percentage : typing___Optional[type___PercentagePolicyConfig] = None,
        model : typing___Optional[type___ModelPolicyConfig] = None,
        sample : typing___Optional[type___SampleIntervalPolicyConfig] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"absolute",b"absolute",u"model",b"model",u"percentage",b"percentage",u"sample",b"sample",u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"absolute",b"absolute",u"model",b"model",u"percentage",b"percentage",u"sample",b"sample",u"value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["absolute","percentage","model","sample"]: ...
type___RetrainPolicyConfig = RetrainPolicyConfig

class AbsolutePolicyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    threshold: builtin___int = ...
    onlyPositives: builtin___bool = ...

    def __init__(self,
        *,
        threshold : typing___Optional[builtin___int] = None,
        onlyPositives : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"onlyPositives",b"onlyPositives",u"threshold",b"threshold"]) -> None: ...
type___AbsolutePolicyConfig = AbsolutePolicyConfig

class PercentagePolicyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    threshold: builtin___float = ...
    onlyPositives: builtin___bool = ...

    def __init__(self,
        *,
        threshold : typing___Optional[builtin___float] = None,
        onlyPositives : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"onlyPositives",b"onlyPositives",u"threshold",b"threshold"]) -> None: ...
type___PercentagePolicyConfig = PercentagePolicyConfig

class ModelPolicyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...
type___ModelPolicyConfig = ModelPolicyConfig

class SampleIntervalPolicyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    num_intervals: builtin___int = ...

    def __init__(self,
        *,
        num_intervals : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"num_intervals",b"num_intervals"]) -> None: ...
type___SampleIntervalPolicyConfig = SampleIntervalPolicyConfig

class Dataset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def frame(self) -> type___FileDataset: ...

    @property
    def random(self) -> type___FileDataset: ...

    @property
    def tile(self) -> type___FileDataset: ...

    @property
    def scope(self) -> type___FileDataset: ...

    @property
    def video(self) -> type___Streaming_Video: ...

    @property
    def network(self) -> type___NetworkDataset: ...

    def __init__(self,
        *,
        frame : typing___Optional[type___FileDataset] = None,
        random : typing___Optional[type___FileDataset] = None,
        tile : typing___Optional[type___FileDataset] = None,
        scope : typing___Optional[type___FileDataset] = None,
        video : typing___Optional[type___Streaming_Video] = None,
        network : typing___Optional[type___NetworkDataset] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"frame",b"frame",u"network",b"network",u"random",b"random",u"scope",b"scope",u"tile",b"tile",u"value",b"value",u"video",b"video"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"frame",b"frame",u"network",b"network",u"random",b"random",u"scope",b"scope",u"tile",b"tile",u"value",b"value",u"video",b"video"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["frame","random","tile","scope","video","network"]: ...
type___Dataset = Dataset

class FileDataset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    dataPath: typing___Text = ...
    tileSize: builtin___int = ...
    numTiles: builtin___int = ...
    timeout: builtin___int = ...
    resizeTile: builtin___bool = ...

    def __init__(self,
        *,
        dataPath : typing___Optional[typing___Text] = None,
        tileSize : typing___Optional[builtin___int] = None,
        numTiles : typing___Optional[builtin___int] = None,
        timeout : typing___Optional[builtin___int] = None,
        resizeTile : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataPath",b"dataPath",u"numTiles",b"numTiles",u"resizeTile",b"resizeTile",u"tileSize",b"tileSize",u"timeout",b"timeout"]) -> None: ...
type___FileDataset = FileDataset

class NetworkDataset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    dataPath: typing___Text = ...
    tileSize: builtin___int = ...
    numTiles: builtin___int = ...
    timeout: builtin___int = ...
    resizeTile: builtin___bool = ...
    dataServerAddr: typing___Text = ...
    dataServerPort: builtin___int = ...
    dataBalanceMode: typing___Text = ...

    def __init__(self,
        *,
        dataPath : typing___Optional[typing___Text] = None,
        tileSize : typing___Optional[builtin___int] = None,
        numTiles : typing___Optional[builtin___int] = None,
        timeout : typing___Optional[builtin___int] = None,
        resizeTile : typing___Optional[builtin___bool] = None,
        dataServerAddr : typing___Optional[typing___Text] = None,
        dataServerPort : typing___Optional[builtin___int] = None,
        dataBalanceMode : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataBalanceMode",b"dataBalanceMode",u"dataPath",b"dataPath",u"dataServerAddr",b"dataServerAddr",u"dataServerPort",b"dataServerPort",u"numTiles",b"numTiles",u"resizeTile",b"resizeTile",u"tileSize",b"tileSize",u"timeout",b"timeout"]) -> None: ...
type___NetworkDataset = NetworkDataset

class Streaming_Video(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    width: builtin___int = ...
    height: builtin___int = ...
    sampling_rate_fps: builtin___int = ...
    video_path: typing___Text = ...
    tile_height: builtin___int = ...
    tile_width: builtin___int = ...

    def __init__(self,
        *,
        width : typing___Optional[builtin___int] = None,
        height : typing___Optional[builtin___int] = None,
        sampling_rate_fps : typing___Optional[builtin___int] = None,
        video_path : typing___Optional[typing___Text] = None,
        tile_height : typing___Optional[builtin___int] = None,
        tile_width : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"height",b"height",u"sampling_rate_fps",b"sampling_rate_fps",u"tile_height",b"tile_height",u"tile_width",b"tile_width",u"video_path",b"video_path",u"width",b"width"]) -> None: ...
type___Streaming_Video = Streaming_Video

class SelectiveConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def topk(self) -> type___TopKConfig: ...

    @property
    def threshold(self) -> type___ThresholdConfig: ...

    @property
    def token(self) -> type___TokenConfig: ...

    @property
    def diversity(self) -> type___DiversityConfig: ...

    def __init__(self,
        *,
        topk : typing___Optional[type___TopKConfig] = None,
        threshold : typing___Optional[type___ThresholdConfig] = None,
        token : typing___Optional[type___TokenConfig] = None,
        diversity : typing___Optional[type___DiversityConfig] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"diversity",b"diversity",u"threshold",b"threshold",u"token",b"token",u"topk",b"topk",u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"diversity",b"diversity",u"threshold",b"threshold",u"token",b"token",u"topk",b"topk",u"value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["topk","threshold","token","diversity"]: ...
type___SelectiveConfig = SelectiveConfig

class TopKConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    k: builtin___int = ...
    batchSize: builtin___int = ...
    countermeasure_threshold: builtin___float = ...
    total_countermeasures: builtin___int = ...

    def __init__(self,
        *,
        k : typing___Optional[builtin___int] = None,
        batchSize : typing___Optional[builtin___int] = None,
        countermeasure_threshold : typing___Optional[builtin___float] = None,
        total_countermeasures : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"batchSize",b"batchSize",u"countermeasure_threshold",b"countermeasure_threshold",u"k",b"k",u"total_countermeasures",b"total_countermeasures"]) -> None: ...
type___TopKConfig = TopKConfig

class ThresholdConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    threshold: builtin___float = ...

    def __init__(self,
        *,
        threshold : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"threshold",b"threshold"]) -> None: ...
type___ThresholdConfig = ThresholdConfig

class TokenConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    initial_samples: builtin___int = ...
    batch_size: builtin___int = ...
    countermeasure_threshold: builtin___float = ...
    total_countermeasures: builtin___int = ...
    upper_threshold_delta: builtin___float = ...
    lower_threshold_delta: builtin___float = ...
    upper_threshold_start: builtin___float = ...
    lower_threshold_start: builtin___float = ...
    sliding_window: builtin___bool = ...

    def __init__(self,
        *,
        initial_samples : typing___Optional[builtin___int] = None,
        batch_size : typing___Optional[builtin___int] = None,
        countermeasure_threshold : typing___Optional[builtin___float] = None,
        total_countermeasures : typing___Optional[builtin___int] = None,
        upper_threshold_delta : typing___Optional[builtin___float] = None,
        lower_threshold_delta : typing___Optional[builtin___float] = None,
        upper_threshold_start : typing___Optional[builtin___float] = None,
        lower_threshold_start : typing___Optional[builtin___float] = None,
        sliding_window : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"batch_size",b"batch_size",u"countermeasure_threshold",b"countermeasure_threshold",u"initial_samples",b"initial_samples",u"lower_threshold_delta",b"lower_threshold_delta",u"lower_threshold_start",b"lower_threshold_start",u"sliding_window",b"sliding_window",u"total_countermeasures",b"total_countermeasures",u"upper_threshold_delta",b"upper_threshold_delta",u"upper_threshold_start",b"upper_threshold_start"]) -> None: ...
type___TokenConfig = TokenConfig

class DiversityConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    k: builtin___int = ...
    batchSize: builtin___int = ...
    countermeasure_threshold: builtin___float = ...
    total_countermeasures: builtin___int = ...

    def __init__(self,
        *,
        k : typing___Optional[builtin___int] = None,
        batchSize : typing___Optional[builtin___int] = None,
        countermeasure_threshold : typing___Optional[builtin___float] = None,
        total_countermeasures : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"batchSize",b"batchSize",u"countermeasure_threshold",b"countermeasure_threshold",u"k",b"k",u"total_countermeasures",b"total_countermeasures"]) -> None: ...
type___DiversityConfig = DiversityConfig

class ReexaminationStrategyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: typing___Text = ...
    k: builtin___int = ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        k : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"k",b"k",u"type",b"type"]) -> None: ...
type___ReexaminationStrategyConfig = ReexaminationStrategyConfig

class NoReexaminationStrategyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___NoReexaminationStrategyConfig = NoReexaminationStrategyConfig

class TopReexaminationStrategyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    k: builtin___int = ...

    def __init__(self,
        *,
        k : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"k",b"k"]) -> None: ...
type___TopReexaminationStrategyConfig = TopReexaminationStrategyConfig

class FullReexaminationStrategyConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___FullReexaminationStrategyConfig = FullReexaminationStrategyConfig

class HawkObject(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AttributesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: builtin___bytes = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[builtin___bytes] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___AttributesEntry = AttributesEntry

    objectId: typing___Text = ...
    content: builtin___bytes = ...

    @property
    def attributes(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, builtin___bytes]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        content : typing___Optional[builtin___bytes] = None,
        attributes : typing___Optional[typing___Mapping[typing___Text, builtin___bytes]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attributes",b"attributes",u"content",b"content",u"objectId",b"objectId"]) -> None: ...
type___HawkObject = HawkObject

class SendTile(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AttributesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: builtin___bytes = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[builtin___bytes] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___AttributesEntry = AttributesEntry

    objectId: typing___Text = ...
    scoutIndex: builtin___int = ...
    version: builtin___int = ...
    feature_vector: builtin___bytes = ...
    novel_sample: builtin___bool = ...

    @property
    def attributes(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, builtin___bytes]: ...

    @property
    def boundingBoxes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___BoundingBox]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        scoutIndex : typing___Optional[builtin___int] = None,
        version : typing___Optional[builtin___int] = None,
        attributes : typing___Optional[typing___Mapping[typing___Text, builtin___bytes]] = None,
        boundingBoxes : typing___Optional[typing___Iterable[type___BoundingBox]] = None,
        feature_vector : typing___Optional[builtin___bytes] = None,
        novel_sample : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attributes",b"attributes",u"boundingBoxes",b"boundingBoxes",u"feature_vector",b"feature_vector",u"novel_sample",b"novel_sample",u"objectId",b"objectId",u"scoutIndex",b"scoutIndex",u"version",b"version"]) -> None: ...
type___SendTile = SendTile

class SendLabel(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId: typing___Text = ...
    scoutIndex: builtin___int = ...

    @property
    def boundingBoxes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___BoundingBox]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        scoutIndex : typing___Optional[builtin___int] = None,
        boundingBoxes : typing___Optional[typing___Iterable[type___BoundingBox]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"boundingBoxes",b"boundingBoxes",u"objectId",b"objectId",u"scoutIndex",b"scoutIndex"]) -> None: ...
type___SendLabel = SendLabel

class LabeledTile(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def obj(self) -> type___HawkObject: ...

    @property
    def boundingBoxes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___BoundingBox]: ...

    def __init__(self,
        *,
        obj : typing___Optional[type___HawkObject] = None,
        boundingBoxes : typing___Optional[typing___Iterable[type___BoundingBox]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"obj",b"obj"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"boundingBoxes",b"boundingBoxes",u"obj",b"obj"]) -> None: ...
type___LabeledTile = LabeledTile

class BoundingBox(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    x: builtin___float = ...
    y: builtin___float = ...
    w: builtin___float = ...
    h: builtin___float = ...
    class_name: typing___Text = ...
    confidence: builtin___float = ...

    def __init__(self,
        *,
        x : typing___Optional[builtin___float] = None,
        y : typing___Optional[builtin___float] = None,
        w : typing___Optional[builtin___float] = None,
        h : typing___Optional[builtin___float] = None,
        class_name : typing___Optional[typing___Text] = None,
        confidence : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"class_name",b"class_name",u"confidence",b"confidence",u"h",b"h",u"w",b"w",u"x",b"x",u"y",b"y"]) -> None: ...
type___BoundingBox = BoundingBox

class PerScoutSCMLOptions(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ScoutDictEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: builtin___int = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[builtin___int] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___ScoutDictEntry = ScoutDictEntry


    @property
    def scout_dict(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, builtin___int]: ...

    def __init__(self,
        *,
        scout_dict : typing___Optional[typing___Mapping[typing___Text, builtin___int]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"scout_dict",b"scout_dict"]) -> None: ...
type___PerScoutSCMLOptions = PerScoutSCMLOptions

class ChangeDeploymentStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ActiveStatus: builtin___bool = ...
    ActiveScoutRatio: builtin___float = ...

    def __init__(self,
        *,
        ActiveStatus : typing___Optional[builtin___bool] = None,
        ActiveScoutRatio : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ActiveScoutRatio",b"ActiveScoutRatio",u"ActiveStatus",b"ActiveStatus"]) -> None: ...
type___ChangeDeploymentStatus = ChangeDeploymentStatus
