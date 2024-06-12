# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x13\x65\x64u.cmu.cs.hawk.api\"\x1a\n\tMissionId\x12\r\n\x05value\x18\x01 \x01(\t\"\xb4\x05\n\x12ScoutConfiguration\x12\x11\n\tmissionId\x18\x01 \x01(\t\x12\x0e\n\x06scouts\x18\x02 \x03(\t\x12\x12\n\nscoutIndex\x18\x03 \x01(\x05\x12\x0e\n\x06homeIP\x18\x04 \x01(\t\x12\x15\n\rtrainLocation\x18\x05 \x01(\t\x12\x18\n\x10missionDirectory\x18\x06 \x01(\t\x12\x37\n\rtrainStrategy\x18\x07 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.TrainConfig\x12?\n\rretrainPolicy\x18\x08 \x01(\x0b\x32(.edu.cmu.cs.hawk.api.RetrainPolicyConfig\x12-\n\x07\x64\x61taset\x18\t \x01(\x0b\x32\x1c.edu.cmu.cs.hawk.api.Dataset\x12\x36\n\x08selector\x18\n \x01(\x0b\x32$.edu.cmu.cs.hawk.api.SelectiveConfig\x12G\n\rreexamination\x18\x0b \x01(\x0b\x32\x30.edu.cmu.cs.hawk.api.ReexaminationStrategyConfig\x12\x37\n\x0cinitialModel\x18\x0c \x01(\x0b\x32!.edu.cmu.cs.hawk.api.ModelArchive\x12\x14\n\x0c\x62ootstrapZip\x18\r \x01(\x0c\x12Q\n\rbandwidthFunc\x18\x0e \x03(\x0b\x32:.edu.cmu.cs.hawk.api.ScoutConfiguration.BandwidthFuncEntry\x12\x10\n\x08validate\x18\x0f \x01(\x08\x12\x12\n\nclass_list\x18\x10 \x03(\t\x1a\x34\n\x12\x42\x61ndwidthFuncEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdc\x01\n\x0cMissionStats\x12\x14\n\x0ctotalObjects\x18\x01 \x01(\x03\x12\x18\n\x10processedObjects\x18\x02 \x01(\x03\x12\x16\n\x0e\x64roppedObjects\x18\x03 \x01(\x03\x12\x16\n\x0e\x66\x61lseNegatives\x18\x04 \x01(\x03\x12=\n\x06others\x18\x05 \x03(\x0b\x32-.edu.cmu.cs.hawk.api.MissionStats.OthersEntry\x1a-\n\x0bOthersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb6\x01\n\x0bTestResults\x12\x14\n\x0ctestExamples\x18\x01 \x01(\x03\x12\x0b\n\x03\x61uc\x18\x02 \x01(\x01\x12\x37\n\x0cmodelMetrics\x18\x03 \x01(\x0b\x32!.edu.cmu.cs.hawk.api.ModelMetrics\x12\x15\n\rbestThreshold\x18\x04 \x01(\x01\x12\x12\n\nprecisions\x18\x05 \x03(\x01\x12\x0f\n\x07recalls\x18\x06 \x03(\x01\x12\x0f\n\x07version\x18\x07 \x01(\x05\"\xa5\x01\n\x0eMissionResults\x12\x41\n\x07results\x18\x01 \x03(\x0b\x32\x30.edu.cmu.cs.hawk.api.MissionResults.ResultsEntry\x1aP\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.TestResults:\x02\x38\x01\"\x89\x01\n\x0cModelMetrics\x12\x15\n\rtruePositives\x18\x01 \x01(\x03\x12\x16\n\x0e\x66\x61lsePositives\x18\x02 \x01(\x03\x12\x16\n\x0e\x66\x61lseNegatives\x18\x03 \x01(\x03\x12\x11\n\tprecision\x18\x04 \x01(\x01\x12\x0e\n\x06recall\x18\x05 \x01(\x01\x12\x0f\n\x07\x66\x31Score\x18\x06 \x01(\x01\"M\n\x0bImportModel\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32!.edu.cmu.cs.hawk.api.ModelArchive\x12\x0c\n\x04path\x18\x02 \x01(\t\"0\n\x0cModelArchive\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x0f\n\x07version\x18\x02 \x01(\x05\"\xaf\x02\n\x0bTrainConfig\x12:\n\x0e\x64nn_classifier\x18\x01 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.ModelConfigH\x00\x12\x30\n\x04yolo\x18\x02 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.ModelConfigH\x00\x12/\n\x03\x66sl\x18\x03 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.ModelConfigH\x00\x12@\n\x14\x64nn_classifier_radar\x18\x04 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.ModelConfigH\x00\x12\x36\n\nyolo_radar\x18\x05 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.ModelConfigH\x00\x42\x07\n\x05value\"t\n\x0bModelConfig\x12\x38\n\x04\x61rgs\x18\x01 \x03(\x0b\x32*.edu.cmu.cs.hawk.api.ModelConfig.ArgsEntry\x1a+\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\nYOLOConfig\x12\x11\n\timageSize\x18\x01 \x01(\x05\x12\x0c\n\x04\x61rgs\x18\x02 \x01(\t\"\x9c\x02\n\x13RetrainPolicyConfig\x12=\n\x08\x61\x62solute\x18\x01 \x01(\x0b\x32).edu.cmu.cs.hawk.api.AbsolutePolicyConfigH\x00\x12\x41\n\npercentage\x18\x02 \x01(\x0b\x32+.edu.cmu.cs.hawk.api.PercentagePolicyConfigH\x00\x12\x37\n\x05model\x18\x03 \x01(\x0b\x32&.edu.cmu.cs.hawk.api.ModelPolicyConfigH\x00\x12\x41\n\x06sample\x18\x04 \x01(\x0b\x32/.edu.cmu.cs.hawk.api.SampleIntervalPolicyConfigH\x00\x42\x07\n\x05value\"@\n\x14\x41\x62solutePolicyConfig\x12\x11\n\tthreshold\x18\x01 \x01(\x05\x12\x15\n\ronlyPositives\x18\x02 \x01(\x08\"B\n\x16PercentagePolicyConfig\x12\x11\n\tthreshold\x18\x01 \x01(\x01\x12\x15\n\ronlyPositives\x18\x02 \x01(\x08\"!\n\x11ModelPolicyConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\"3\n\x1aSampleIntervalPolicyConfig\x12\x15\n\rnum_intervals\x18\x01 \x01(\x05\"\x95\x02\n\x07\x44\x61taset\x12\x31\n\x05\x66rame\x18\x01 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.FileDatasetH\x00\x12\x32\n\x06random\x18\x02 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.FileDatasetH\x00\x12\x30\n\x04tile\x18\x03 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.FileDatasetH\x00\x12\x31\n\x05scope\x18\x04 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.FileDatasetH\x00\x12\x35\n\x05video\x18\x05 \x01(\x0b\x32$.edu.cmu.cs.hawk.api.Streaming_VideoH\x00\x42\x07\n\x05value\"h\n\x0b\x46ileDataset\x12\x10\n\x08\x64\x61taPath\x18\x01 \x01(\t\x12\x10\n\x08tileSize\x18\x02 \x01(\x05\x12\x10\n\x08numTiles\x18\x03 \x01(\x05\x12\x0f\n\x07timeout\x18\x04 \x01(\x05\x12\x12\n\nresizeTile\x18\x05 \x01(\x08\"k\n\x0eNetworkDataset\x12\x16\n\x0e\x64\x61taSourceAddr\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x61taSourcePort\x18\x02 \x01(\x05\x12\x15\n\rretrievalRate\x18\x03 \x01(\x01\x12\x12\n\nresizeTile\x18\x05 \x01(\x08\"\x88\x01\n\x0fStreaming_Video\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x19\n\x11sampling_rate_fps\x18\x03 \x01(\x05\x12\x12\n\nvideo_path\x18\x04 \x01(\t\x12\x13\n\x0btile_height\x18\x05 \x01(\x05\x12\x12\n\ntile_width\x18\x06 \x01(\x05\"\xf4\x01\n\x0fSelectiveConfig\x12/\n\x04topk\x18\x01 \x01(\x0b\x32\x1f.edu.cmu.cs.hawk.api.TopKConfigH\x00\x12\x39\n\tthreshold\x18\x02 \x01(\x0b\x32$.edu.cmu.cs.hawk.api.ThresholdConfigH\x00\x12\x31\n\x05token\x18\x03 \x01(\x0b\x32 .edu.cmu.cs.hawk.api.TokenConfigH\x00\x12\x39\n\tdiversity\x18\x04 \x01(\x0b\x32$.edu.cmu.cs.hawk.api.DiversityConfigH\x00\x42\x07\n\x05value\"k\n\nTopKConfig\x12\t\n\x01k\x18\x01 \x01(\x05\x12\x11\n\tbatchSize\x18\x02 \x01(\x05\x12 \n\x18\x63ountermeasure_threshold\x18\x03 \x01(\x01\x12\x1d\n\x15total_countermeasures\x18\x04 \x01(\x05\"$\n\x0fThresholdConfig\x12\x11\n\tthreshold\x18\x01 \x01(\x01\"{\n\x0bTokenConfig\x12\x17\n\x0finitial_samples\x18\x01 \x01(\x05\x12\x12\n\nbatch_size\x18\x02 \x01(\x05\x12 \n\x18\x63ountermeasure_threshold\x18\x03 \x01(\x01\x12\x1d\n\x15total_countermeasures\x18\x04 \x01(\x05\"p\n\x0f\x44iversityConfig\x12\t\n\x01k\x18\x01 \x01(\x05\x12\x11\n\tbatchSize\x18\x02 \x01(\x05\x12 \n\x18\x63ountermeasure_threshold\x18\x03 \x01(\x01\x12\x1d\n\x15total_countermeasures\x18\x04 \x01(\x05\"6\n\x1bReexaminationStrategyConfig\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\t\n\x01k\x18\x02 \x01(\x05\"\x1f\n\x1dNoReexaminationStrategyConfig\"+\n\x1eTopReexaminationStrategyConfig\x12\t\n\x01k\x18\x01 \x01(\x05\"!\n\x1f\x46ullReexaminationStrategyConfig\"R\n\x0cTileMetadata\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x30\n\x05label\x18\x02 \x01(\x0b\x32!.edu.cmu.cs.hawk.api.LabelWrapper\"m\n\x0bLabeledTile\x12,\n\x03obj\x18\x01 \x01(\x0b\x32\x1f.edu.cmu.cs.hawk.api.HawkObject\x12\x30\n\x05label\x18\x02 \x01(\x0b\x32!.edu.cmu.cs.hawk.api.LabelWrapper\"@\n\x0cTokenMessage\x12\x30\n\x05label\x18\x01 \x01(\x0b\x32!.edu.cmu.cs.hawk.api.LabelWrapper\"_\n\x0cLabelWrapper\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\nscoutIndex\x18\x02 \x01(\x05\x12\x12\n\nimageLabel\x18\x03 \x01(\t\x12\x15\n\rboundingBoxes\x18\x04 \x03(\t\"\xa7\x01\n\nHawkObject\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x43\n\nattributes\x18\x03 \x03(\x0b\x32/.edu.cmu.cs.hawk.api.HawkObject.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xc8\x01\n\tSendTiles\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\nscoutIndex\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x01\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x42\n\nattributes\x18\x05 \x03(\x0b\x32..edu.cmu.cs.hawk.api.SendTiles.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\">\n\nSendLabels\x12\x30\n\x05label\x18\x01 \x01(\x0b\x32!.edu.cmu.cs.hawk.api.LabelWrapper*#\n\x0c\x44\x61tasetSplit\x12\t\n\x05TRAIN\x10\x00\x12\x08\n\x04TEST\x10\x01\x42\x02P\x01\x62\x06proto3')

_DATASETSPLIT = DESCRIPTOR.enum_types_by_name['DatasetSplit']
DatasetSplit = enum_type_wrapper.EnumTypeWrapper(_DATASETSPLIT)
TRAIN = 0
TEST = 1


_MISSIONID = DESCRIPTOR.message_types_by_name['MissionId']
_SCOUTCONFIGURATION = DESCRIPTOR.message_types_by_name['ScoutConfiguration']
_SCOUTCONFIGURATION_BANDWIDTHFUNCENTRY = _SCOUTCONFIGURATION.nested_types_by_name['BandwidthFuncEntry']
_MISSIONSTATS = DESCRIPTOR.message_types_by_name['MissionStats']
_MISSIONSTATS_OTHERSENTRY = _MISSIONSTATS.nested_types_by_name['OthersEntry']
_TESTRESULTS = DESCRIPTOR.message_types_by_name['TestResults']
_MISSIONRESULTS = DESCRIPTOR.message_types_by_name['MissionResults']
_MISSIONRESULTS_RESULTSENTRY = _MISSIONRESULTS.nested_types_by_name['ResultsEntry']
_MODELMETRICS = DESCRIPTOR.message_types_by_name['ModelMetrics']
_IMPORTMODEL = DESCRIPTOR.message_types_by_name['ImportModel']
_MODELARCHIVE = DESCRIPTOR.message_types_by_name['ModelArchive']
_TRAINCONFIG = DESCRIPTOR.message_types_by_name['TrainConfig']
_MODELCONFIG = DESCRIPTOR.message_types_by_name['ModelConfig']
_MODELCONFIG_ARGSENTRY = _MODELCONFIG.nested_types_by_name['ArgsEntry']
_YOLOCONFIG = DESCRIPTOR.message_types_by_name['YOLOConfig']
_RETRAINPOLICYCONFIG = DESCRIPTOR.message_types_by_name['RetrainPolicyConfig']
_ABSOLUTEPOLICYCONFIG = DESCRIPTOR.message_types_by_name['AbsolutePolicyConfig']
_PERCENTAGEPOLICYCONFIG = DESCRIPTOR.message_types_by_name['PercentagePolicyConfig']
_MODELPOLICYCONFIG = DESCRIPTOR.message_types_by_name['ModelPolicyConfig']
_SAMPLEINTERVALPOLICYCONFIG = DESCRIPTOR.message_types_by_name['SampleIntervalPolicyConfig']
_DATASET = DESCRIPTOR.message_types_by_name['Dataset']
_FILEDATASET = DESCRIPTOR.message_types_by_name['FileDataset']
_NETWORKDATASET = DESCRIPTOR.message_types_by_name['NetworkDataset']
_STREAMING_VIDEO = DESCRIPTOR.message_types_by_name['Streaming_Video']
_SELECTIVECONFIG = DESCRIPTOR.message_types_by_name['SelectiveConfig']
_TOPKCONFIG = DESCRIPTOR.message_types_by_name['TopKConfig']
_THRESHOLDCONFIG = DESCRIPTOR.message_types_by_name['ThresholdConfig']
_TOKENCONFIG = DESCRIPTOR.message_types_by_name['TokenConfig']
_DIVERSITYCONFIG = DESCRIPTOR.message_types_by_name['DiversityConfig']
_REEXAMINATIONSTRATEGYCONFIG = DESCRIPTOR.message_types_by_name['ReexaminationStrategyConfig']
_NOREEXAMINATIONSTRATEGYCONFIG = DESCRIPTOR.message_types_by_name['NoReexaminationStrategyConfig']
_TOPREEXAMINATIONSTRATEGYCONFIG = DESCRIPTOR.message_types_by_name['TopReexaminationStrategyConfig']
_FULLREEXAMINATIONSTRATEGYCONFIG = DESCRIPTOR.message_types_by_name['FullReexaminationStrategyConfig']
_TILEMETADATA = DESCRIPTOR.message_types_by_name['TileMetadata']
_LABELEDTILE = DESCRIPTOR.message_types_by_name['LabeledTile']
_TOKENMESSAGE = DESCRIPTOR.message_types_by_name['TokenMessage']
_LABELWRAPPER = DESCRIPTOR.message_types_by_name['LabelWrapper']
_HAWKOBJECT = DESCRIPTOR.message_types_by_name['HawkObject']
_HAWKOBJECT_ATTRIBUTESENTRY = _HAWKOBJECT.nested_types_by_name['AttributesEntry']
_SENDTILES = DESCRIPTOR.message_types_by_name['SendTiles']
_SENDTILES_ATTRIBUTESENTRY = _SENDTILES.nested_types_by_name['AttributesEntry']
_SENDLABELS = DESCRIPTOR.message_types_by_name['SendLabels']
MissionId = _reflection.GeneratedProtocolMessageType('MissionId', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONID,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.MissionId)
  })
_sym_db.RegisterMessage(MissionId)

ScoutConfiguration = _reflection.GeneratedProtocolMessageType('ScoutConfiguration', (_message.Message,), {

  'BandwidthFuncEntry' : _reflection.GeneratedProtocolMessageType('BandwidthFuncEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCOUTCONFIGURATION_BANDWIDTHFUNCENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ScoutConfiguration.BandwidthFuncEntry)
    })
  ,
  'DESCRIPTOR' : _SCOUTCONFIGURATION,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ScoutConfiguration)
  })
_sym_db.RegisterMessage(ScoutConfiguration)
_sym_db.RegisterMessage(ScoutConfiguration.BandwidthFuncEntry)

MissionStats = _reflection.GeneratedProtocolMessageType('MissionStats', (_message.Message,), {

  'OthersEntry' : _reflection.GeneratedProtocolMessageType('OthersEntry', (_message.Message,), {
    'DESCRIPTOR' : _MISSIONSTATS_OTHERSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.MissionStats.OthersEntry)
    })
  ,
  'DESCRIPTOR' : _MISSIONSTATS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.MissionStats)
  })
_sym_db.RegisterMessage(MissionStats)
_sym_db.RegisterMessage(MissionStats.OthersEntry)

TestResults = _reflection.GeneratedProtocolMessageType('TestResults', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESULTS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TestResults)
  })
_sym_db.RegisterMessage(TestResults)

MissionResults = _reflection.GeneratedProtocolMessageType('MissionResults', (_message.Message,), {

  'ResultsEntry' : _reflection.GeneratedProtocolMessageType('ResultsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MISSIONRESULTS_RESULTSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.MissionResults.ResultsEntry)
    })
  ,
  'DESCRIPTOR' : _MISSIONRESULTS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.MissionResults)
  })
_sym_db.RegisterMessage(MissionResults)
_sym_db.RegisterMessage(MissionResults.ResultsEntry)

ModelMetrics = _reflection.GeneratedProtocolMessageType('ModelMetrics', (_message.Message,), {
  'DESCRIPTOR' : _MODELMETRICS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ModelMetrics)
  })
_sym_db.RegisterMessage(ModelMetrics)

ImportModel = _reflection.GeneratedProtocolMessageType('ImportModel', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTMODEL,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ImportModel)
  })
_sym_db.RegisterMessage(ImportModel)

ModelArchive = _reflection.GeneratedProtocolMessageType('ModelArchive', (_message.Message,), {
  'DESCRIPTOR' : _MODELARCHIVE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ModelArchive)
  })
_sym_db.RegisterMessage(ModelArchive)

TrainConfig = _reflection.GeneratedProtocolMessageType('TrainConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRAINCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TrainConfig)
  })
_sym_db.RegisterMessage(TrainConfig)

ModelConfig = _reflection.GeneratedProtocolMessageType('ModelConfig', (_message.Message,), {

  'ArgsEntry' : _reflection.GeneratedProtocolMessageType('ArgsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MODELCONFIG_ARGSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ModelConfig.ArgsEntry)
    })
  ,
  'DESCRIPTOR' : _MODELCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ModelConfig)
  })
_sym_db.RegisterMessage(ModelConfig)
_sym_db.RegisterMessage(ModelConfig.ArgsEntry)

YOLOConfig = _reflection.GeneratedProtocolMessageType('YOLOConfig', (_message.Message,), {
  'DESCRIPTOR' : _YOLOCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.YOLOConfig)
  })
_sym_db.RegisterMessage(YOLOConfig)

RetrainPolicyConfig = _reflection.GeneratedProtocolMessageType('RetrainPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _RETRAINPOLICYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.RetrainPolicyConfig)
  })
_sym_db.RegisterMessage(RetrainPolicyConfig)

AbsolutePolicyConfig = _reflection.GeneratedProtocolMessageType('AbsolutePolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _ABSOLUTEPOLICYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.AbsolutePolicyConfig)
  })
_sym_db.RegisterMessage(AbsolutePolicyConfig)

PercentagePolicyConfig = _reflection.GeneratedProtocolMessageType('PercentagePolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _PERCENTAGEPOLICYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.PercentagePolicyConfig)
  })
_sym_db.RegisterMessage(PercentagePolicyConfig)

ModelPolicyConfig = _reflection.GeneratedProtocolMessageType('ModelPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _MODELPOLICYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ModelPolicyConfig)
  })
_sym_db.RegisterMessage(ModelPolicyConfig)

SampleIntervalPolicyConfig = _reflection.GeneratedProtocolMessageType('SampleIntervalPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEINTERVALPOLICYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.SampleIntervalPolicyConfig)
  })
_sym_db.RegisterMessage(SampleIntervalPolicyConfig)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

FileDataset = _reflection.GeneratedProtocolMessageType('FileDataset', (_message.Message,), {
  'DESCRIPTOR' : _FILEDATASET,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.FileDataset)
  })
_sym_db.RegisterMessage(FileDataset)

NetworkDataset = _reflection.GeneratedProtocolMessageType('NetworkDataset', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKDATASET,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.NetworkDataset)
  })
_sym_db.RegisterMessage(NetworkDataset)

Streaming_Video = _reflection.GeneratedProtocolMessageType('Streaming_Video', (_message.Message,), {
  'DESCRIPTOR' : _STREAMING_VIDEO,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.Streaming_Video)
  })
_sym_db.RegisterMessage(Streaming_Video)

SelectiveConfig = _reflection.GeneratedProtocolMessageType('SelectiveConfig', (_message.Message,), {
  'DESCRIPTOR' : _SELECTIVECONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.SelectiveConfig)
  })
_sym_db.RegisterMessage(SelectiveConfig)

TopKConfig = _reflection.GeneratedProtocolMessageType('TopKConfig', (_message.Message,), {
  'DESCRIPTOR' : _TOPKCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TopKConfig)
  })
_sym_db.RegisterMessage(TopKConfig)

ThresholdConfig = _reflection.GeneratedProtocolMessageType('ThresholdConfig', (_message.Message,), {
  'DESCRIPTOR' : _THRESHOLDCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ThresholdConfig)
  })
_sym_db.RegisterMessage(ThresholdConfig)

TokenConfig = _reflection.GeneratedProtocolMessageType('TokenConfig', (_message.Message,), {
  'DESCRIPTOR' : _TOKENCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TokenConfig)
  })
_sym_db.RegisterMessage(TokenConfig)

DiversityConfig = _reflection.GeneratedProtocolMessageType('DiversityConfig', (_message.Message,), {
  'DESCRIPTOR' : _DIVERSITYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.DiversityConfig)
  })
_sym_db.RegisterMessage(DiversityConfig)

ReexaminationStrategyConfig = _reflection.GeneratedProtocolMessageType('ReexaminationStrategyConfig', (_message.Message,), {
  'DESCRIPTOR' : _REEXAMINATIONSTRATEGYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.ReexaminationStrategyConfig)
  })
_sym_db.RegisterMessage(ReexaminationStrategyConfig)

NoReexaminationStrategyConfig = _reflection.GeneratedProtocolMessageType('NoReexaminationStrategyConfig', (_message.Message,), {
  'DESCRIPTOR' : _NOREEXAMINATIONSTRATEGYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.NoReexaminationStrategyConfig)
  })
_sym_db.RegisterMessage(NoReexaminationStrategyConfig)

TopReexaminationStrategyConfig = _reflection.GeneratedProtocolMessageType('TopReexaminationStrategyConfig', (_message.Message,), {
  'DESCRIPTOR' : _TOPREEXAMINATIONSTRATEGYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TopReexaminationStrategyConfig)
  })
_sym_db.RegisterMessage(TopReexaminationStrategyConfig)

FullReexaminationStrategyConfig = _reflection.GeneratedProtocolMessageType('FullReexaminationStrategyConfig', (_message.Message,), {
  'DESCRIPTOR' : _FULLREEXAMINATIONSTRATEGYCONFIG,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.FullReexaminationStrategyConfig)
  })
_sym_db.RegisterMessage(FullReexaminationStrategyConfig)

TileMetadata = _reflection.GeneratedProtocolMessageType('TileMetadata', (_message.Message,), {
  'DESCRIPTOR' : _TILEMETADATA,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TileMetadata)
  })
_sym_db.RegisterMessage(TileMetadata)

LabeledTile = _reflection.GeneratedProtocolMessageType('LabeledTile', (_message.Message,), {
  'DESCRIPTOR' : _LABELEDTILE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.LabeledTile)
  })
_sym_db.RegisterMessage(LabeledTile)

TokenMessage = _reflection.GeneratedProtocolMessageType('TokenMessage', (_message.Message,), {
  'DESCRIPTOR' : _TOKENMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.TokenMessage)
  })
_sym_db.RegisterMessage(TokenMessage)

LabelWrapper = _reflection.GeneratedProtocolMessageType('LabelWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LABELWRAPPER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.LabelWrapper)
  })
_sym_db.RegisterMessage(LabelWrapper)

HawkObject = _reflection.GeneratedProtocolMessageType('HawkObject', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HAWKOBJECT_ATTRIBUTESENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.HawkObject.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _HAWKOBJECT,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.HawkObject)
  })
_sym_db.RegisterMessage(HawkObject)
_sym_db.RegisterMessage(HawkObject.AttributesEntry)

SendTiles = _reflection.GeneratedProtocolMessageType('SendTiles', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SENDTILES_ATTRIBUTESENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.SendTiles.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _SENDTILES,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.SendTiles)
  })
_sym_db.RegisterMessage(SendTiles)
_sym_db.RegisterMessage(SendTiles.AttributesEntry)

SendLabels = _reflection.GeneratedProtocolMessageType('SendLabels', (_message.Message,), {
  'DESCRIPTOR' : _SENDLABELS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:edu.cmu.cs.hawk.api.SendLabels)
  })
_sym_db.RegisterMessage(SendLabels)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _SCOUTCONFIGURATION_BANDWIDTHFUNCENTRY._options = None
  _SCOUTCONFIGURATION_BANDWIDTHFUNCENTRY._serialized_options = b'8\001'
  _MISSIONSTATS_OTHERSENTRY._options = None
  _MISSIONSTATS_OTHERSENTRY._serialized_options = b'8\001'
  _MISSIONRESULTS_RESULTSENTRY._options = None
  _MISSIONRESULTS_RESULTSENTRY._serialized_options = b'8\001'
  _MODELCONFIG_ARGSENTRY._options = None
  _MODELCONFIG_ARGSENTRY._serialized_options = b'8\001'
  _HAWKOBJECT_ATTRIBUTESENTRY._options = None
  _HAWKOBJECT_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _SENDTILES_ATTRIBUTESENTRY._options = None
  _SENDTILES_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _DATASETSPLIT._serialized_start=4818
  _DATASETSPLIT._serialized_end=4853
  _MISSIONID._serialized_start=39
  _MISSIONID._serialized_end=65
  _SCOUTCONFIGURATION._serialized_start=68
  _SCOUTCONFIGURATION._serialized_end=760
  _SCOUTCONFIGURATION_BANDWIDTHFUNCENTRY._serialized_start=708
  _SCOUTCONFIGURATION_BANDWIDTHFUNCENTRY._serialized_end=760
  _MISSIONSTATS._serialized_start=763
  _MISSIONSTATS._serialized_end=983
  _MISSIONSTATS_OTHERSENTRY._serialized_start=938
  _MISSIONSTATS_OTHERSENTRY._serialized_end=983
  _TESTRESULTS._serialized_start=986
  _TESTRESULTS._serialized_end=1168
  _MISSIONRESULTS._serialized_start=1171
  _MISSIONRESULTS._serialized_end=1336
  _MISSIONRESULTS_RESULTSENTRY._serialized_start=1256
  _MISSIONRESULTS_RESULTSENTRY._serialized_end=1336
  _MODELMETRICS._serialized_start=1339
  _MODELMETRICS._serialized_end=1476
  _IMPORTMODEL._serialized_start=1478
  _IMPORTMODEL._serialized_end=1555
  _MODELARCHIVE._serialized_start=1557
  _MODELARCHIVE._serialized_end=1605
  _TRAINCONFIG._serialized_start=1608
  _TRAINCONFIG._serialized_end=1911
  _MODELCONFIG._serialized_start=1913
  _MODELCONFIG._serialized_end=2029
  _MODELCONFIG_ARGSENTRY._serialized_start=1986
  _MODELCONFIG_ARGSENTRY._serialized_end=2029
  _YOLOCONFIG._serialized_start=2031
  _YOLOCONFIG._serialized_end=2076
  _RETRAINPOLICYCONFIG._serialized_start=2079
  _RETRAINPOLICYCONFIG._serialized_end=2363
  _ABSOLUTEPOLICYCONFIG._serialized_start=2365
  _ABSOLUTEPOLICYCONFIG._serialized_end=2429
  _PERCENTAGEPOLICYCONFIG._serialized_start=2431
  _PERCENTAGEPOLICYCONFIG._serialized_end=2497
  _MODELPOLICYCONFIG._serialized_start=2499
  _MODELPOLICYCONFIG._serialized_end=2532
  _SAMPLEINTERVALPOLICYCONFIG._serialized_start=2534
  _SAMPLEINTERVALPOLICYCONFIG._serialized_end=2585
  _DATASET._serialized_start=2588
  _DATASET._serialized_end=2865
  _FILEDATASET._serialized_start=2867
  _FILEDATASET._serialized_end=2971
  _NETWORKDATASET._serialized_start=2973
  _NETWORKDATASET._serialized_end=3080
  _STREAMING_VIDEO._serialized_start=3083
  _STREAMING_VIDEO._serialized_end=3219
  _SELECTIVECONFIG._serialized_start=3222
  _SELECTIVECONFIG._serialized_end=3466
  _TOPKCONFIG._serialized_start=3468
  _TOPKCONFIG._serialized_end=3575
  _THRESHOLDCONFIG._serialized_start=3577
  _THRESHOLDCONFIG._serialized_end=3613
  _TOKENCONFIG._serialized_start=3615
  _TOKENCONFIG._serialized_end=3738
  _DIVERSITYCONFIG._serialized_start=3740
  _DIVERSITYCONFIG._serialized_end=3852
  _REEXAMINATIONSTRATEGYCONFIG._serialized_start=3854
  _REEXAMINATIONSTRATEGYCONFIG._serialized_end=3908
  _NOREEXAMINATIONSTRATEGYCONFIG._serialized_start=3910
  _NOREEXAMINATIONSTRATEGYCONFIG._serialized_end=3941
  _TOPREEXAMINATIONSTRATEGYCONFIG._serialized_start=3943
  _TOPREEXAMINATIONSTRATEGYCONFIG._serialized_end=3986
  _FULLREEXAMINATIONSTRATEGYCONFIG._serialized_start=3988
  _FULLREEXAMINATIONSTRATEGYCONFIG._serialized_end=4021
  _TILEMETADATA._serialized_start=4023
  _TILEMETADATA._serialized_end=4105
  _LABELEDTILE._serialized_start=4107
  _LABELEDTILE._serialized_end=4216
  _TOKENMESSAGE._serialized_start=4218
  _TOKENMESSAGE._serialized_end=4282
  _LABELWRAPPER._serialized_start=4284
  _LABELWRAPPER._serialized_end=4379
  _HAWKOBJECT._serialized_start=4382
  _HAWKOBJECT._serialized_end=4549
  _HAWKOBJECT_ATTRIBUTESENTRY._serialized_start=4500
  _HAWKOBJECT_ATTRIBUTESENTRY._serialized_end=4549
  _SENDTILES._serialized_start=4552
  _SENDTILES._serialized_end=4752
  _SENDTILES_ATTRIBUTESENTRY._serialized_start=4500
  _SENDTILES_ATTRIBUTESENTRY._serialized_end=4549
  _SENDLABELS._serialized_start=4754
  _SENDLABELS._serialized_end=4816
# @@protoc_insertion_point(module_scope)
