# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/resource/wallet/v3.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9takasho/schema/common_featureset/resource/wallet/v3.proto\x12\x33takasho.schema.common_featureset.resource.wallet.v3\"\xcf\x03\n\x06Wallet\x12g\n\x12virtual_currencies\x18\x01 \x03(\x0b\x32K.takasho.schema.common_featureset.resource.wallet.v3.Wallet.VirtualCurrency\x12\x65\n\x11player_key_values\x18\x02 \x03(\x0b\x32J.takasho.schema.common_featureset.resource.wallet.v3.Wallet.PlayerKeyValue\x1a\x98\x01\n\x0fVirtualCurrency\x12\x1d\n\x15virtual_currency_name\x18\x01 \x01(\t\x12V\n\x08platform\x18\x02 \x01(\x0e\x32\x44.takasho.schema.common_featureset.resource.wallet.v3.Wallet.Platform\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x12\x1a-\n\x0ePlayerKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x12\"+\n\x08Platform\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x41PPLE\x10\x01\x12\n\n\x06GOOGLE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.resource.wallet.v3_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WALLET._serialized_start=115
  _WALLET._serialized_end=578
  _WALLET_VIRTUALCURRENCY._serialized_start=334
  _WALLET_VIRTUALCURRENCY._serialized_end=486
  _WALLET_PLAYERKEYVALUE._serialized_start=488
  _WALLET_PLAYERKEYVALUE._serialized_end=533
  _WALLET_PLATFORM._serialized_start=535
  _WALLET_PLATFORM._serialized_end=578
# @@protoc_insertion_point(module_scope)