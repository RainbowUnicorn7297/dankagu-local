# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/player_api/player_storage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__storage_dot_v2__pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__event__log_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@takasho/schema/common_featureset/player_api/player_storage.proto\x12+takasho.schema.common_featureset.player_api\x1a\x41takasho/schema/common_featureset/resource/player_storage/v2.proto\x1a\x43takasho/schema/common_featureset/resource/player_event_log/v1.proto\"\x8b\x03\n\x19PlayerStorageSetEntriesV2\x1a\xfa\x01\n\x07Request\x12S\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x42.takasho.schema.common_featureset.resource.player_storage.v2.Entry\x12\x15\n\rnext_revision\x18\x02 \x01(\t\x12\x19\n\x11previous_revision\x18\x03 \x01(\t\x12h\n\x11player_event_logs\x18\x04 \x03(\x0b\x32M.takasho.schema.common_featureset.resource.player_event_log.v1.PlayerEventLog\x1aq\n\x08Response\x12S\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x42.takasho.schema.common_featureset.resource.player_storage.v2.Entry\x12\x10\n\x08revision\x18\x02 \x01(\t\"\xf3\x01\n\x19PlayerStorageGetEntriesV2\x1a\x63\n\x07Request\x12X\n\x08\x63riteria\x18\x01 \x03(\x0b\x32\x46.takasho.schema.common_featureset.resource.player_storage.v2.Criterion\x1aq\n\x08Response\x12S\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x42.takasho.schema.common_featureset.resource.player_storage.v2.Entry\x12\x10\n\x08revision\x18\x02 \x01(\t\"\x80\x02\n$PlayerStorageGetOtherPlayerEntriesV2\x1aw\n\x07Request\x12\x12\n\nplayer_ids\x18\x01 \x03(\t\x12X\n\x08\x63riteria\x18\x02 \x03(\x0b\x32\x46.takasho.schema.common_featureset.resource.player_storage.v2.Criterion\x1a_\n\x08Response\x12S\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x42.takasho.schema.common_featureset.resource.player_storage.v2.Entry2\xcc\x04\n\rPlayerStorage\x12\xb1\x01\n\x0cSetEntriesV2\x12N.takasho.schema.common_featureset.player_api.PlayerStorageSetEntriesV2.Request\x1aO.takasho.schema.common_featureset.player_api.PlayerStorageSetEntriesV2.Response\"\x00\x12\xb1\x01\n\x0cGetEntriesV2\x12N.takasho.schema.common_featureset.player_api.PlayerStorageGetEntriesV2.Request\x1aO.takasho.schema.common_featureset.player_api.PlayerStorageGetEntriesV2.Response\"\x00\x12\xd2\x01\n\x17GetOtherPlayerEntriesV2\x12Y.takasho.schema.common_featureset.player_api.PlayerStorageGetOtherPlayerEntriesV2.Request\x1aZ.takasho.schema.common_featureset.player_api.PlayerStorageGetOtherPlayerEntriesV2.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.player_api.player_storage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERSTORAGESETENTRIESV2._serialized_start=250
  _PLAYERSTORAGESETENTRIESV2._serialized_end=645
  _PLAYERSTORAGESETENTRIESV2_REQUEST._serialized_start=280
  _PLAYERSTORAGESETENTRIESV2_REQUEST._serialized_end=530
  _PLAYERSTORAGESETENTRIESV2_RESPONSE._serialized_start=532
  _PLAYERSTORAGESETENTRIESV2_RESPONSE._serialized_end=645
  _PLAYERSTORAGEGETENTRIESV2._serialized_start=648
  _PLAYERSTORAGEGETENTRIESV2._serialized_end=891
  _PLAYERSTORAGEGETENTRIESV2_REQUEST._serialized_start=677
  _PLAYERSTORAGEGETENTRIESV2_REQUEST._serialized_end=776
  _PLAYERSTORAGEGETENTRIESV2_RESPONSE._serialized_start=532
  _PLAYERSTORAGEGETENTRIESV2_RESPONSE._serialized_end=645
  _PLAYERSTORAGEGETOTHERPLAYERENTRIESV2._serialized_start=894
  _PLAYERSTORAGEGETOTHERPLAYERENTRIESV2._serialized_end=1150
  _PLAYERSTORAGEGETOTHERPLAYERENTRIESV2_REQUEST._serialized_start=934
  _PLAYERSTORAGEGETOTHERPLAYERENTRIESV2_REQUEST._serialized_end=1053
  _PLAYERSTORAGEGETOTHERPLAYERENTRIESV2_RESPONSE._serialized_start=532
  _PLAYERSTORAGEGETOTHERPLAYERENTRIESV2_RESPONSE._serialized_end=627
  _PLAYERSTORAGE._serialized_start=1153
  _PLAYERSTORAGE._serialized_end=1741
# @@protoc_insertion_point(module_scope)