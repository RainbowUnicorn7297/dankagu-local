# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/resource/consume_resource_set/v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGtakasho/schema/common_featureset/resource/consume_resource_set/v1.proto\x12\x41takasho.schema.common_featureset.resource.consume_resource_set.v1\"\x9c\x02\n\x12\x43onsumeResourceSet\x12\x1f\n\x17\x63onsume_resource_set_id\x18\x01 \x01(\t\x12\x66\n\rresource_type\x18\x02 \x01(\x0e\x32O.takasho.schema.common_featureset.resource.consume_resource_set.v1.ResourceType\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x12\x12m\n\x11\x63onsume_resources\x18\x04 \x03(\x0b\x32R.takasho.schema.common_featureset.resource.consume_resource_set.v1.ConsumeResource\"V\n\x0f\x43onsumeResource\x12\x1b\n\x13\x63onsume_resource_id\x18\x01 \x01(\t\x12\x14\n\x0cresource_key\x18\x02 \x01(\t\x12\x10\n\x08priority\x18\x03 \x01(\x12*J\n\x0cResourceType\x12\x14\n\x10VIRTUAL_CURRENCY\x10\x00\x12\x14\n\x10PLAYER_KEY_VALUE\x10\x01\x12\x0e\n\nNO_CONSUME\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.resource.consume_resource_set.v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESOURCETYPE._serialized_start=517
  _RESOURCETYPE._serialized_end=591
  _CONSUMERESOURCESET._serialized_start=143
  _CONSUMERESOURCESET._serialized_end=427
  _CONSUMERESOURCE._serialized_start=429
  _CONSUMERESOURCE._serialized_end=515
# @@protoc_insertion_point(module_scope)
