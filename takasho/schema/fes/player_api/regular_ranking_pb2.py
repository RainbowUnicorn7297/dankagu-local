# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/fes/player_api/regular_ranking.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.fes.resource.player_regular_ranking import v1_pb2 as takasho_dot_schema_dot_fes_dot_resource_dot_player__regular__ranking_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3takasho/schema/fes/player_api/regular_ranking.proto\x12\x1dtakasho.schema.fes.player_api\x1a;takasho/schema/fes/resource/player_regular_ranking/v1.proto\"\xba\x01\n\x18RegularRankingRegisterV1\x1a-\n\x07Request\x12\x13\n\x0branking_key\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x03\x1ao\n\x08Response\x12\x63\n\x0eplayer_ranking\x18\x01 \x01(\x0b\x32K.takasho.schema.fes.resource.player_regular_ranking.v1.PlayerRegularRanking\"\xcf\x01\n\x1dRegularRankingGetTopRankingV1\x1a<\n\x07Request\x12\x13\n\x0branking_key\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x12\x12\r\n\x05\x63ount\x18\x03 \x01(\x12\x1ap\n\x08Response\x12\x64\n\x0fplayer_rankings\x18\x01 \x03(\x0b\x32K.takasho.schema.fes.resource.player_regular_ranking.v1.PlayerRegularRanking2\xc7\x02\n\x0eRegularRanking\x12\x91\x01\n\nRegisterV1\x12?.takasho.schema.fes.player_api.RegularRankingRegisterV1.Request\x1a@.takasho.schema.fes.player_api.RegularRankingRegisterV1.Response\"\x00\x12\xa0\x01\n\x0fGetTopRankingV1\x12\x44.takasho.schema.fes.player_api.RegularRankingGetTopRankingV1.Request\x1a\x45.takasho.schema.fes.player_api.RegularRankingGetTopRankingV1.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.fes.player_api.regular_ranking_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGULARRANKINGREGISTERV1._serialized_start=148
  _REGULARRANKINGREGISTERV1._serialized_end=334
  _REGULARRANKINGREGISTERV1_REQUEST._serialized_start=176
  _REGULARRANKINGREGISTERV1_REQUEST._serialized_end=221
  _REGULARRANKINGREGISTERV1_RESPONSE._serialized_start=223
  _REGULARRANKINGREGISTERV1_RESPONSE._serialized_end=334
  _REGULARRANKINGGETTOPRANKINGV1._serialized_start=337
  _REGULARRANKINGGETTOPRANKINGV1._serialized_end=544
  _REGULARRANKINGGETTOPRANKINGV1_REQUEST._serialized_start=370
  _REGULARRANKINGGETTOPRANKINGV1_REQUEST._serialized_end=430
  _REGULARRANKINGGETTOPRANKINGV1_RESPONSE._serialized_start=432
  _REGULARRANKINGGETTOPRANKINGV1_RESPONSE._serialized_end=544
  _REGULARRANKING._serialized_start=547
  _REGULARRANKING._serialized_end=874
# @@protoc_insertion_point(module_scope)
