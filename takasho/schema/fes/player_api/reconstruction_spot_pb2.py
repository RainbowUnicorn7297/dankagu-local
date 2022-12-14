# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/fes/player_api/reconstruction_spot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.fes.resource.reconstruction_spot import v1_pb2 as takasho_dot_schema_dot_fes_dot_resource_dot_reconstruction__spot_dot_v1__pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__event__log_dot_v1__pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__inventory_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7takasho/schema/fes/player_api/reconstruction_spot.proto\x12\x1dtakasho.schema.fes.player_api\x1a\x38takasho/schema/fes/resource/reconstruction_spot/v1.proto\x1a\x43takasho/schema/common_featureset/resource/player_event_log/v1.proto\x1a\x43takasho/schema/common_featureset/resource/player_inventory/v1.proto\"\x82\x01\n ReconstructionSpotGetAvailableV1\x1a\t\n\x07Request\x1aS\n\x08Response\x12G\n\x05spots\x18\x01 \x03(\x0b\x32\x38.takasho.schema.fes.resource.reconstruction_spot.v1.Spot\"\x89\x02\n!ReconstructionSpotReceivePrizesV1\x1as\n\x07Request\x12h\n\x11player_event_logs\x18\x01 \x03(\x0b\x32M.takasho.schema.common_featureset.resource.player_event_log.v1.PlayerEventLog\x1ao\n\x08Response\x12\x63\n\x0binventories\x18\x01 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory2\xe7\x02\n\x12ReconstructionSpot\x12\xa5\x01\n\x0eGetAvailableV1\x12G.takasho.schema.fes.player_api.ReconstructionSpotGetAvailableV1.Request\x1aH.takasho.schema.fes.player_api.ReconstructionSpotGetAvailableV1.Response\"\x00\x12\xa8\x01\n\x0fReceivePrizesV1\x12H.takasho.schema.fes.player_api.ReconstructionSpotReceivePrizesV1.Request\x1aI.takasho.schema.fes.player_api.ReconstructionSpotReceivePrizesV1.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.fes.player_api.reconstruction_spot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECONSTRUCTIONSPOTGETAVAILABLEV1._serialized_start=287
  _RECONSTRUCTIONSPOTGETAVAILABLEV1._serialized_end=417
  _RECONSTRUCTIONSPOTGETAVAILABLEV1_REQUEST._serialized_start=323
  _RECONSTRUCTIONSPOTGETAVAILABLEV1_REQUEST._serialized_end=332
  _RECONSTRUCTIONSPOTGETAVAILABLEV1_RESPONSE._serialized_start=334
  _RECONSTRUCTIONSPOTGETAVAILABLEV1_RESPONSE._serialized_end=417
  _RECONSTRUCTIONSPOTRECEIVEPRIZESV1._serialized_start=420
  _RECONSTRUCTIONSPOTRECEIVEPRIZESV1._serialized_end=685
  _RECONSTRUCTIONSPOTRECEIVEPRIZESV1_REQUEST._serialized_start=457
  _RECONSTRUCTIONSPOTRECEIVEPRIZESV1_REQUEST._serialized_end=572
  _RECONSTRUCTIONSPOTRECEIVEPRIZESV1_RESPONSE._serialized_start=574
  _RECONSTRUCTIONSPOTRECEIVEPRIZESV1_RESPONSE._serialized_end=685
  _RECONSTRUCTIONSPOT._serialized_start=688
  _RECONSTRUCTIONSPOT._serialized_end=1047
# @@protoc_insertion_point(module_scope)
