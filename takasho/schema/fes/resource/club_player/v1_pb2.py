# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/fes/resource/club_player/v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__storage_dot_v2__pb2
from takasho.schema.fes.resource.club_role import v1_pb2 as takasho_dot_schema_dot_fes_dot_resource_dot_club__role_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0takasho/schema/fes/resource/club_player/v1.proto\x12*takasho.schema.fes.resource.club_player.v1\x1a\x41takasho/schema/common_featureset/resource/player_storage/v2.proto\x1a.takasho/schema/fes/resource/club_role/v1.proto\"\xad\x02\n\nClubPlayer\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x62\n\x16player_storage_entries\x18\x02 \x03(\x0b\x32\x42.takasho.schema.common_featureset.resource.player_storage.v2.Entry\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\r\n\x05\x66rame\x18\x04 \x01(\x04\x12@\n\x04role\x18\x05 \x01(\x0e\x32\x32.takasho.schema.fes.resource.club_role.v1.ClubRole\x12\x11\n\tjoined_at\x18\x06 \x01(\x12\x12\x19\n\x11last_logged_in_at\x18\x07 \x01(\x12\x12\x17\n\x0fplayer_short_id\x18\x08 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.fes.resource.club_player.v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLUBPLAYER._serialized_start=212
  _CLUBPLAYER._serialized_end=513
# @@protoc_insertion_point(module_scope)