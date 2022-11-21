# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/resource/player_event_log/v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCtakasho/schema/common_featureset/resource/player_event_log/v1.proto\x12=takasho.schema.common_featureset.resource.player_event_log.v1\"}\n\x0ePlayerEventLog\x12\x16\n\x0e\x65vent_category\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x14\n\x0cplayer_state\x18\x04 \x01(\t\x12\x1a\n\x12player_state_bytes\x18\x05 \x01(\x0c\"2\n\x1bPlayerEventLogServerPayload\x12\x13\n\x0btakasho_log\x18\x01 \x01(\x0c\"\xfa\x01\n\tLootBoxV3\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x1b\n\x13loot_box_product_id\x18\x02 \x01(\t\x12\x0b\n\x03num\x18\x03 \x01(\x03\x12\x13\n\x0b\x63ontent_ids\x18\x04 \x03(\t\x12i\n\x11\x63onsume_resources\x18\x05 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_event_log.v1.ConsumeResource\x12\x16\n\x0e\x63ontent_values\x18\x06 \x03(\x0c\x12\x13\n\x0btakasho_log\x18\x07 \x01(\x0c\"\x9c\x02\n\x0fStepUpLootBoxV2\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12#\n\x1bstep_up_loot_box_product_id\x18\x02 \x01(\t\x12\x0c\n\x04step\x18\x03 \x01(\x03\x12\x11\n\tnext_step\x18\x04 \x01(\x03\x12\x13\n\x0b\x63ontent_ids\x18\x05 \x03(\t\x12i\n\x11\x63onsume_resources\x18\x06 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_event_log.v1.ConsumeResource\x12\x16\n\x0e\x63ontent_values\x18\x07 \x03(\x0c\x12\x13\n\x0btakasho_log\x18\x08 \x01(\x0c\"M\n\x0f\x43onsumeResource\x12\x1c\n\x14\x63onsume_resource_key\x18\x01 \x01(\t\x12\x1c\n\x14\x63onsume_resource_num\x18\x02 \x01(\x03\"\xae\x02\n\x08\x46riendV1\x12g\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32R.takasho.schema.common_featureset.resource.player_event_log.v1.FriendV1.ActionType\x12\x19\n\x11target_player_ids\x18\x02 \x03(\t\x12\x13\n\x0b\x66riends_num\x18\x03 \x01(\x03\x12\x17\n\x0fmax_friends_num\x18\x04 \x01(\x03\x12\x13\n\x0btakasho_log\x18\x05 \x01(\x0c\"[\n\nActionType\x12\x08\n\x04SEND\x10\x00\x12\x0b\n\x07\x41PPROVE\x10\x01\x12\n\n\x06REJECT\x10\x02\x12\x11\n\rDELETE_FRIEND\x10\x03\x12\x17\n\x13\x44\x45LETE_SENT_REQUEST\x10\x04\"\xbd\x01\n\tConsumeVc\x12\n\n\x02id\x18\x01 \x01(\t\x12\x65\n\ncurrencies\x18\x02 \x03(\x0b\x32Q.takasho.schema.common_featureset.resource.player_event_log.v1.ConsumeVc.Currency\x12\x13\n\x0btakasho_log\x18\x03 \x01(\x0c\x1a(\n\x08\x43urrency\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61monut\x18\x02 \x01(\x03\"\xb0\x01\n\nBoxLootBox\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x10\n\x08gacha_id\x18\x02 \x01(\t\x12\x10\n\x08\x65xec_num\x18\x03 \x01(\x03\x12\x14\n\x0cget_item_ids\x18\x04 \x03(\t\x12\x0f\n\x07paid_id\x18\x05 \x01(\t\x12\x13\n\x0bpaid_amount\x18\x06 \x01(\x03\x12\x15\n\raf_box_remain\x18\x07 \x01(\x03\x12\x13\n\x0btakasho_log\x18\x08 \x01(\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.resource.player_event_log.v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYEREVENTLOG._serialized_start=134
  _PLAYEREVENTLOG._serialized_end=259
  _PLAYEREVENTLOGSERVERPAYLOAD._serialized_start=261
  _PLAYEREVENTLOGSERVERPAYLOAD._serialized_end=311
  _LOOTBOXV3._serialized_start=314
  _LOOTBOXV3._serialized_end=564
  _STEPUPLOOTBOXV2._serialized_start=567
  _STEPUPLOOTBOXV2._serialized_end=851
  _CONSUMERESOURCE._serialized_start=853
  _CONSUMERESOURCE._serialized_end=930
  _FRIENDV1._serialized_start=933
  _FRIENDV1._serialized_end=1235
  _FRIENDV1_ACTIONTYPE._serialized_start=1144
  _FRIENDV1_ACTIONTYPE._serialized_end=1235
  _CONSUMEVC._serialized_start=1238
  _CONSUMEVC._serialized_end=1427
  _CONSUMEVC_CURRENCY._serialized_start=1387
  _CONSUMEVC_CURRENCY._serialized_end=1427
  _BOXLOOTBOX._serialized_start=1430
  _BOXLOOTBOX._serialized_end=1606
# @@protoc_insertion_point(module_scope)