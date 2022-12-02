# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: takasho/schema/common_featureset/player_api/loot_box.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from takasho.schema.common_featureset.resource.loot_box import v3_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_loot__box_dot_v3__pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__inventory_dot_v1__pb2
from takasho.schema.common_featureset.resource.wallet import v3_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_wallet_dot_v3__pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as takasho_dot_schema_dot_common__featureset_dot_resource_dot_player__event__log_dot_v1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:takasho/schema/common_featureset/player_api/loot_box.proto\x12+takasho.schema.common_featureset.player_api\x1a;takasho/schema/common_featureset/resource/loot_box/v3.proto\x1a\x43takasho/schema/common_featureset/resource/player_inventory/v1.proto\x1a\x39takasho/schema/common_featureset/resource/wallet/v3.proto\x1a\x43takasho/schema/common_featureset/resource/player_event_log/v1.proto\"\x90\x01\n\x15LootBoxGetAvailableV1\x1a\t\n\x07Request\x1al\n\x08Response\x12`\n\x11loot_box_products\x18\x01 \x03(\x0b\x32\x45.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProduct\"\x93\x03\n\x11LootBoxPurchaseV1\x1a>\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x1a\xbd\x02\n\x08Response\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12`\n\x11loot_box_contents\x18\x02 \x03(\x0b\x32\x45.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxContent\x12j\n\x12player_inventories\x18\x03 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\x12K\n\x06wallet\x18\x04 \x01(\x0b\x32;.takasho.schema.common_featureset.resource.wallet.v3.Wallet\"\xb6\x01\n\x17LootBoxGetProbabilityV1\x1a&\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x1as\n\x08Response\x12g\n\x14loot_box_probability\x18\x01 \x01(\x0b\x32I.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProbability\"\xc2\x02\n\x12LootBoxGetDetailV1\x1a&\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x1a\x83\x02\n\x08Response\x12_\n\x10loot_box_product\x18\x01 \x01(\x0b\x32\x45.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProduct\x12g\n\x15loot_box_content_sets\x18\x02 \x03(\x0b\x32H.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxContentSet\x12\x12\n\nis_limited\x18\x03 \x01(\x08\x12\x19\n\x11purchasable_count\x18\x04 \x01(\x12\"\x80\x02\n\x17LootBoxV2GetAvailableV1\x1a\x32\n\x07Request\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x04\x1a\xb0\x01\n\x08Response\x12r\n\x11loot_box_products\x18\x01 \x03(\x0b\x32W.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProductWithPurchasedCount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\"\xbe\x06\n\x13LootBoxV2PurchaseV1\x1a\xe8\x01\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x12l\n\rresource_type\x18\x03 \x01(\x0e\x32U.takasho.schema.common_featureset.player_api.LootBoxV2PurchaseV1.Request.ResourceType\":\n\x0cResourceType\x12\x14\n\x10VIRTUAL_CURRENCY\x10\x00\x12\x14\n\x10PLAYER_KEY_VALUE\x10\x01\x1a\xbb\x04\n\x08Response\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12s\n\x1bloot_box_content_set_prizes\x18\x02 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxContentSetPrizes\x12j\n\x12player_inventories\x18\x03 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\x12p\n\x18\x65xtra_player_inventories\x18\x04 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\x12K\n\x06wallet\x18\x05 \x01(\x0b\x32;.takasho.schema.common_featureset.resource.wallet.v3.Wallet\x12w\n\x1fpickup_extra_player_inventories\x18\x06 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\"\xb8\x01\n\x19LootBoxV2GetProbabilityV1\x1a&\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x1as\n\x08Response\x12g\n\x14loot_box_probability\x18\x01 \x01(\x0b\x32I.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProbability\"\xa1\x03\n\x14LootBoxV2GetDetailV1\x1a&\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x1a\xe0\x02\n\x08Response\x12_\n\x10loot_box_product\x18\x01 \x01(\x0b\x32\x45.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProduct\x12g\n\x15loot_box_content_sets\x18\x02 \x03(\x0b\x32H.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxContentSet\x12\x12\n\nis_limited\x18\x03 \x01(\x08\x12\x17\n\x0fpurchased_count\x18\x04 \x01(\x12\x12]\n\x0floot_box_pickup\x18\x05 \x01(\x0b\x32\x44.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxPickup\"\xa1\x02\n\x17LootBoxV3GetAvailableV1\x1aS\n\x07Request\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x04\x12\x1f\n\x17\x65xclude_pickup_response\x18\x03 \x01(\x08\x1a\xb0\x01\n\x08Response\x12r\n\x11loot_box_products\x18\x01 \x03(\x0b\x32W.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProductWithPurchasedCount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x17\n\x0fprev_page_token\x18\x03 \x01(\t\"\xe6\x07\n\x13LootBoxV3PurchaseV1\x1a\x90\x03\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x12l\n\rresource_type\x18\x03 \x01(\x0e\x32U.takasho.schema.common_featureset.player_api.LootBoxV3PurchaseV1.Request.ResourceType\x12\x16\n\x0epurchase_token\x18\x04 \x01(\t\x12\x14\n\x0cpurchase_num\x18\x05 \x01(\x12\x12h\n\x11player_event_logs\x18\x06 \x03(\x0b\x32M.takasho.schema.common_featureset.resource.player_event_log.v1.PlayerEventLog\"J\n\x0cResourceType\x12\x14\n\x10VIRTUAL_CURRENCY\x10\x00\x12\x14\n\x10PLAYER_KEY_VALUE\x10\x01\x12\x0e\n\nNO_CONSUME\x10\x02\x1a\xbb\x04\n\x08Response\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12s\n\x1bloot_box_content_set_prizes\x18\x02 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxContentSetPrizes\x12j\n\x12player_inventories\x18\x03 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\x12p\n\x18\x65xtra_player_inventories\x18\x04 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\x12K\n\x06wallet\x18\x05 \x01(\x0b\x32;.takasho.schema.common_featureset.resource.wallet.v3.Wallet\x12w\n\x1fpickup_extra_player_inventories\x18\x06 \x03(\x0b\x32N.takasho.schema.common_featureset.resource.player_inventory.v1.PlayerInventory\"\xd1\x01\n\x19LootBoxV3GetProbabilityV1\x1a&\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x1a\x8b\x01\n\x08Response\x12g\n\x14loot_box_probability\x18\x01 \x01(\x0b\x32I.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProbability\x12\x16\n\x0epurchase_token\x18\x02 \x01(\t\"\xa1\x03\n\x14LootBoxV3GetDetailV1\x1a&\n\x07Request\x12\x1b\n\x13loot_box_product_id\x18\x01 \x01(\t\x1a\xe0\x02\n\x08Response\x12_\n\x10loot_box_product\x18\x01 \x01(\x0b\x32\x45.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxProduct\x12g\n\x15loot_box_content_sets\x18\x02 \x03(\x0b\x32H.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxContentSet\x12\x12\n\nis_limited\x18\x03 \x01(\x08\x12\x17\n\x0fpurchased_count\x18\x04 \x01(\x12\x12]\n\x0floot_box_pickup\x18\x05 \x01(\x0b\x32\x44.takasho.schema.common_featureset.resource.loot_box.v3.LootBoxPickup2\xb2\x05\n\x07LootBox\x12\xab\x01\n\x0eGetAvailableV1\x12J.takasho.schema.common_featureset.player_api.LootBoxGetAvailableV1.Request\x1aK.takasho.schema.common_featureset.player_api.LootBoxGetAvailableV1.Response\"\x00\x12\x9f\x01\n\nPurchaseV1\x12\x46.takasho.schema.common_featureset.player_api.LootBoxPurchaseV1.Request\x1aG.takasho.schema.common_featureset.player_api.LootBoxPurchaseV1.Response\"\x00\x12\xb1\x01\n\x10GetProbabilityV1\x12L.takasho.schema.common_featureset.player_api.LootBoxGetProbabilityV1.Request\x1aM.takasho.schema.common_featureset.player_api.LootBoxGetProbabilityV1.Response\"\x00\x12\xa2\x01\n\x0bGetDetailV1\x12G.takasho.schema.common_featureset.player_api.LootBoxGetDetailV1.Request\x1aH.takasho.schema.common_featureset.player_api.LootBoxGetDetailV1.Response\"\x00\x32\xc4\x05\n\tLootBoxV2\x12\xaf\x01\n\x0eGetAvailableV1\x12L.takasho.schema.common_featureset.player_api.LootBoxV2GetAvailableV1.Request\x1aM.takasho.schema.common_featureset.player_api.LootBoxV2GetAvailableV1.Response\"\x00\x12\xa3\x01\n\nPurchaseV1\x12H.takasho.schema.common_featureset.player_api.LootBoxV2PurchaseV1.Request\x1aI.takasho.schema.common_featureset.player_api.LootBoxV2PurchaseV1.Response\"\x00\x12\xb5\x01\n\x10GetProbabilityV1\x12N.takasho.schema.common_featureset.player_api.LootBoxV2GetProbabilityV1.Request\x1aO.takasho.schema.common_featureset.player_api.LootBoxV2GetProbabilityV1.Response\"\x00\x12\xa6\x01\n\x0bGetDetailV1\x12I.takasho.schema.common_featureset.player_api.LootBoxV2GetDetailV1.Request\x1aJ.takasho.schema.common_featureset.player_api.LootBoxV2GetDetailV1.Response\"\x00\x32\xc4\x05\n\tLootBoxV3\x12\xaf\x01\n\x0eGetAvailableV1\x12L.takasho.schema.common_featureset.player_api.LootBoxV3GetAvailableV1.Request\x1aM.takasho.schema.common_featureset.player_api.LootBoxV3GetAvailableV1.Response\"\x00\x12\xa3\x01\n\nPurchaseV1\x12H.takasho.schema.common_featureset.player_api.LootBoxV3PurchaseV1.Request\x1aI.takasho.schema.common_featureset.player_api.LootBoxV3PurchaseV1.Response\"\x00\x12\xb5\x01\n\x10GetProbabilityV1\x12N.takasho.schema.common_featureset.player_api.LootBoxV3GetProbabilityV1.Request\x1aO.takasho.schema.common_featureset.player_api.LootBoxV3GetProbabilityV1.Response\"\x00\x12\xa6\x01\n\x0bGetDetailV1\x12I.takasho.schema.common_featureset.player_api.LootBoxV3GetDetailV1.Request\x1aJ.takasho.schema.common_featureset.player_api.LootBoxV3GetDetailV1.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'takasho.schema.common_featureset.player_api.loot_box_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOOTBOXGETAVAILABLEV1._serialized_start=366
  _LOOTBOXGETAVAILABLEV1._serialized_end=510
  _LOOTBOXGETAVAILABLEV1_REQUEST._serialized_start=391
  _LOOTBOXGETAVAILABLEV1_REQUEST._serialized_end=400
  _LOOTBOXGETAVAILABLEV1_RESPONSE._serialized_start=402
  _LOOTBOXGETAVAILABLEV1_RESPONSE._serialized_end=510
  _LOOTBOXPURCHASEV1._serialized_start=513
  _LOOTBOXPURCHASEV1._serialized_end=916
  _LOOTBOXPURCHASEV1_REQUEST._serialized_start=534
  _LOOTBOXPURCHASEV1_REQUEST._serialized_end=596
  _LOOTBOXPURCHASEV1_RESPONSE._serialized_start=599
  _LOOTBOXPURCHASEV1_RESPONSE._serialized_end=916
  _LOOTBOXGETPROBABILITYV1._serialized_start=919
  _LOOTBOXGETPROBABILITYV1._serialized_end=1101
  _LOOTBOXGETPROBABILITYV1_REQUEST._serialized_start=534
  _LOOTBOXGETPROBABILITYV1_REQUEST._serialized_end=572
  _LOOTBOXGETPROBABILITYV1_RESPONSE._serialized_start=986
  _LOOTBOXGETPROBABILITYV1_RESPONSE._serialized_end=1101
  _LOOTBOXGETDETAILV1._serialized_start=1104
  _LOOTBOXGETDETAILV1._serialized_end=1426
  _LOOTBOXGETDETAILV1_REQUEST._serialized_start=534
  _LOOTBOXGETDETAILV1_REQUEST._serialized_end=572
  _LOOTBOXGETDETAILV1_RESPONSE._serialized_start=1167
  _LOOTBOXGETDETAILV1_RESPONSE._serialized_end=1426
  _LOOTBOXV2GETAVAILABLEV1._serialized_start=1429
  _LOOTBOXV2GETAVAILABLEV1._serialized_end=1685
  _LOOTBOXV2GETAVAILABLEV1_REQUEST._serialized_start=1456
  _LOOTBOXV2GETAVAILABLEV1_REQUEST._serialized_end=1506
  _LOOTBOXV2GETAVAILABLEV1_RESPONSE._serialized_start=1509
  _LOOTBOXV2GETAVAILABLEV1_RESPONSE._serialized_end=1685
  _LOOTBOXV2PURCHASEV1._serialized_start=1688
  _LOOTBOXV2PURCHASEV1._serialized_end=2518
  _LOOTBOXV2PURCHASEV1_REQUEST._serialized_start=1712
  _LOOTBOXV2PURCHASEV1_REQUEST._serialized_end=1944
  _LOOTBOXV2PURCHASEV1_REQUEST_RESOURCETYPE._serialized_start=1886
  _LOOTBOXV2PURCHASEV1_REQUEST_RESOURCETYPE._serialized_end=1944
  _LOOTBOXV2PURCHASEV1_RESPONSE._serialized_start=1947
  _LOOTBOXV2PURCHASEV1_RESPONSE._serialized_end=2518
  _LOOTBOXV2GETPROBABILITYV1._serialized_start=2521
  _LOOTBOXV2GETPROBABILITYV1._serialized_end=2705
  _LOOTBOXV2GETPROBABILITYV1_REQUEST._serialized_start=534
  _LOOTBOXV2GETPROBABILITYV1_REQUEST._serialized_end=572
  _LOOTBOXV2GETPROBABILITYV1_RESPONSE._serialized_start=986
  _LOOTBOXV2GETPROBABILITYV1_RESPONSE._serialized_end=1101
  _LOOTBOXV2GETDETAILV1._serialized_start=2708
  _LOOTBOXV2GETDETAILV1._serialized_end=3125
  _LOOTBOXV2GETDETAILV1_REQUEST._serialized_start=534
  _LOOTBOXV2GETDETAILV1_REQUEST._serialized_end=572
  _LOOTBOXV2GETDETAILV1_RESPONSE._serialized_start=2773
  _LOOTBOXV2GETDETAILV1_RESPONSE._serialized_end=3125
  _LOOTBOXV3GETAVAILABLEV1._serialized_start=3128
  _LOOTBOXV3GETAVAILABLEV1._serialized_end=3417
  _LOOTBOXV3GETAVAILABLEV1_REQUEST._serialized_start=3155
  _LOOTBOXV3GETAVAILABLEV1_REQUEST._serialized_end=3238
  _LOOTBOXV3GETAVAILABLEV1_RESPONSE._serialized_start=1509
  _LOOTBOXV3GETAVAILABLEV1_RESPONSE._serialized_end=1685
  _LOOTBOXV3PURCHASEV1._serialized_start=3420
  _LOOTBOXV3PURCHASEV1._serialized_end=4418
  _LOOTBOXV3PURCHASEV1_REQUEST._serialized_start=3444
  _LOOTBOXV3PURCHASEV1_REQUEST._serialized_end=3844
  _LOOTBOXV3PURCHASEV1_REQUEST_RESOURCETYPE._serialized_start=3770
  _LOOTBOXV3PURCHASEV1_REQUEST_RESOURCETYPE._serialized_end=3844
  _LOOTBOXV3PURCHASEV1_RESPONSE._serialized_start=1947
  _LOOTBOXV3PURCHASEV1_RESPONSE._serialized_end=2518
  _LOOTBOXV3GETPROBABILITYV1._serialized_start=4421
  _LOOTBOXV3GETPROBABILITYV1._serialized_end=4630
  _LOOTBOXV3GETPROBABILITYV1_REQUEST._serialized_start=534
  _LOOTBOXV3GETPROBABILITYV1_REQUEST._serialized_end=572
  _LOOTBOXV3GETPROBABILITYV1_RESPONSE._serialized_start=4491
  _LOOTBOXV3GETPROBABILITYV1_RESPONSE._serialized_end=4630
  _LOOTBOXV3GETDETAILV1._serialized_start=4633
  _LOOTBOXV3GETDETAILV1._serialized_end=5050
  _LOOTBOXV3GETDETAILV1_REQUEST._serialized_start=534
  _LOOTBOXV3GETDETAILV1_REQUEST._serialized_end=572
  _LOOTBOXV3GETDETAILV1_RESPONSE._serialized_start=2773
  _LOOTBOXV3GETDETAILV1_RESPONSE._serialized_end=3125
  _LOOTBOX._serialized_start=5053
  _LOOTBOX._serialized_end=5743
  _LOOTBOXV2._serialized_start=5746
  _LOOTBOXV2._serialized_end=6454
  _LOOTBOXV3._serialized_start=6457
  _LOOTBOXV3._serialized_end=7165
# @@protoc_insertion_point(module_scope)
