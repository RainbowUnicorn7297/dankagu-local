# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/fes/player_api/login_bonus.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.fes.resource.login_bonus import v1_pb2 as takasho_dot_schema_dot_fes_dot_resource_dot_login__bonus_dot_v1__pb2
from takasho.schema.common_featureset.resource.login_bonus import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_login__bonus_dot_v1__pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__inventory_dot_v1__pb2
from takasho.schema.fes.resource.comeback_login_bonus import v1_pb2 as takasho_dot_schema_dot_fes_dot_resource_dot_comeback__login__bonus_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/takasho/schema/fes/player_api/login_bonus.proto\x12\x1dtakasho.schema.fes.player_api\x1a\x30takasho/schema/fes/resource/login_bonus/v1.proto\x1a>takasho/schema/common_featureset/resource/login_bonus/v1.proto\x1a\x43takasho/schema/common_featureset/resource/player_inventory/v1.proto\x1a\x39takasho/schema/fes/resource/comeback_login_bonus/v1.proto\"\xc2\x04\n\x1bLoginBonusCountUpProgressV1\x1a\t\n\x07Request\x1a\x97\x04\n\x08Response\x12X\n\x13\x62ingo_login_bonuses\x18\x01 \x03(\x0b\x32;.takasho.schema.fes.resource.login_bonus.v1.BingoLoginBonus\x12\x64\n\x16\x63\x61mpaign_login_bonuses\x18\x02 \x03(\x0b\x32\x44.takasho.schema.common_featureset.resource.login_bonus.v1.LoginBonus\x12j\n\x12player_inventories\x18\x03 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\x12\x65\n\x14\x63omeback_login_bonus\x18\x04 \x03(\x0b\x32G.takasho.schema.fes.resource.comeback_login_bonus.v1.ComebackLoginBonus\x12x\n\x1f\x63omeback_login_bonus_progresses\x18\x05 \x03(\x0b\x32O.takasho.schema.fes.resource.comeback_login_bonus.v1.ComebackLoginBonusProgress\"\xed\x02\n\x18LoginBonusGetAvailableV1\x1a\t\n\x07Request\x1a\xc5\x02\n\x08Response\x12X\n\x13\x62ingo_login_bonuses\x18\x01 \x03(\x0b\x32;.takasho.schema.fes.resource.login_bonus.v1.BingoLoginBonus\x12\x65\n\x14\x63omeback_login_bonus\x18\x02 \x03(\x0b\x32G.takasho.schema.fes.resource.comeback_login_bonus.v1.ComebackLoginBonus\x12x\n\x1f\x63omeback_login_bonus_progresses\x18\x03 \x03(\x0b\x32O.takasho.schema.fes.resource.comeback_login_bonus.v1.ComebackLoginBonusProgress2\xcf\x02\n\nLoginBonus\x12\x9e\x01\n\x11\x43ountUpProgressV1\x12\x42.takasho.schema.fes.player_api.LoginBonusCountUpProgressV1.Request\x1a\x43.takasho.schema.fes.player_api.LoginBonusCountUpProgressV1.Response\"\x00\x12\x9f\x01\n\x18GetAvailableLoginBonusV1\x12?.takasho.schema.fes.player_api.LoginBonusGetAvailableV1.Request\x1a@.takasho.schema.fes.player_api.LoginBonusGetAvailableV1.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.fes.player_api.login_bonus_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINBONUSCOUNTUPPROGRESSV1._serialized_start=325
  _LOGINBONUSCOUNTUPPROGRESSV1._serialized_end=903
  _LOGINBONUSCOUNTUPPROGRESSV1_REQUEST._serialized_start=356
  _LOGINBONUSCOUNTUPPROGRESSV1_REQUEST._serialized_end=365
  _LOGINBONUSCOUNTUPPROGRESSV1_RESPONSE._serialized_start=368
  _LOGINBONUSCOUNTUPPROGRESSV1_RESPONSE._serialized_end=903
  _LOGINBONUSGETAVAILABLEV1._serialized_start=906
  _LOGINBONUSGETAVAILABLEV1._serialized_end=1271
  _LOGINBONUSGETAVAILABLEV1_REQUEST._serialized_start=356
  _LOGINBONUSGETAVAILABLEV1_REQUEST._serialized_end=365
  _LOGINBONUSGETAVAILABLEV1_RESPONSE._serialized_start=946
  _LOGINBONUSGETAVAILABLEV1_RESPONSE._serialized_end=1271
  _LOGINBONUS._serialized_start=1274
  _LOGINBONUS._serialized_end=1609
# @@protoc_insertion_point(module_scope)
