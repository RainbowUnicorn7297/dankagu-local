# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/player_api/wallet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.common_featureset.resource.wallet import v3_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_wallet_dot_v3__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8takasho/schema/common_featureset/player_api/wallet.proto\x12+takasho.schema.common_featureset.player_api\x1a\x39takasho/schema/common_featureset/resource/wallet/v3.proto\"~\n\x13WalletGetBalancesV1\x1a\t\n\x07Request\x1aX\n\x08Response\x12L\n\x07\x62\x61lance\x18\x01 \x03(\x0b\x32;.takasho.schema.common_featureset.resource.wallet.v3.Wallet:\x02\x18\x01\"\xf2\x01\n\x13WalletGetBalancesV2\x1a\x1d\n\x07Request\x12\x12\n\nexpired_at\x18\x01 \x01(\x03\x1a\xbb\x01\n\x08Response\x12J\n\x05total\x18\x01 \x01(\x0b\x32;.takasho.schema.common_featureset.resource.wallet.v3.Wallet\x12O\n\nexpiration\x18\x02 \x01(\x0b\x32;.takasho.schema.common_featureset.resource.wallet.v3.Wallet\x12\x12\n\nexpired_at\x18\x03 \x01(\x03\x32\xda\x02\n\x06Wallet\x12\xa6\x01\n\rGetBalancesV1\x12H.takasho.schema.common_featureset.player_api.WalletGetBalancesV1.Request\x1aI.takasho.schema.common_featureset.player_api.WalletGetBalancesV1.Response\"\x00\x12\xa6\x01\n\rGetBalancesV2\x12H.takasho.schema.common_featureset.player_api.WalletGetBalancesV2.Request\x1aI.takasho.schema.common_featureset.player_api.WalletGetBalancesV2.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.player_api.wallet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WALLETGETBALANCESV1._options = None
  _WALLETGETBALANCESV1._serialized_options = b'\030\001'
  _WALLETGETBALANCESV1._serialized_start=164
  _WALLETGETBALANCESV1._serialized_end=290
  _WALLETGETBALANCESV1_REQUEST._serialized_start=187
  _WALLETGETBALANCESV1_REQUEST._serialized_end=196
  _WALLETGETBALANCESV1_RESPONSE._serialized_start=198
  _WALLETGETBALANCESV1_RESPONSE._serialized_end=286
  _WALLETGETBALANCESV2._serialized_start=293
  _WALLETGETBALANCESV2._serialized_end=535
  _WALLETGETBALANCESV2_REQUEST._serialized_start=316
  _WALLETGETBALANCESV2_REQUEST._serialized_end=345
  _WALLETGETBALANCESV2_RESPONSE._serialized_start=348
  _WALLETGETBALANCESV2_RESPONSE._serialized_end=535
  _WALLET._serialized_start=538
  _WALLET._serialized_end=884
# @@protoc_insertion_point(module_scope)