# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/resource/player_storage/v2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAtakasho/schema/common_featureset/resource/player_storage/v2.proto\x12;takasho.schema.common_featureset.resource.player_storage.v2\"^\n\x05\x45ntry\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x0c\x12\x12\n\ncreated_at\x18\x04 \x01(\x12\x12\x12\n\nupdated_at\x18\x05 \x01(\x12\"\xac\x01\n\tCriterion\x12\x0b\n\x03key\x18\x01 \x01(\t\x12j\n\rmatching_type\x18\x02 \x01(\x0e\x32S.takasho.schema.common_featureset.resource.player_storage.v2.Criterion.MatchingType\"&\n\x0cMatchingType\x12\t\n\x05\x45XACT\x10\x00\x12\x0b\n\x07\x46ORWARD\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.resource.player_storage.v2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTRY._serialized_start=130
  _ENTRY._serialized_end=224
  _CRITERION._serialized_start=227
  _CRITERION._serialized_end=399
  _CRITERION_MATCHINGTYPE._serialized_start=361
  _CRITERION_MATCHINGTYPE._serialized_end=399
# @@protoc_insertion_point(module_scope)
