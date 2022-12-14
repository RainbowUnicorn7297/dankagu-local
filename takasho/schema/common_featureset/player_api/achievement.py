import time

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import achievement_pb2
from takasho.schema.common_featureset.player_api import achievement_pb2_grpc
from takasho.shared_storage import shared_storage


class Achievement(achievement_pb2_grpc.AchievementServicer):

    def UnlockAndSavePlayerStorageV1(self, request, context):
        response = achievement_pb2.AchievementUnlockAndSavePlayerStorageV1.Response()
        # if 'Mission_10019_211' in request.achievement_ids:
        #     player_achievement = response.player_achievements.add()
        #     achievement = player_achievement.achievement
        #     achievement.achievement_id = 'Mission_10019_211'
        #     achievement.value = b'{"Name":"Mission_10019","Value":211}'
        #     achievement.opened_at = 1665601200
        #     achievement.closed_at = 1666954799
        #     achievement.date_line = '04:00:00Z'
        #     prize = achievement.prizes.add()
        #     prize.achievement_id = 'Mission_10019_211'
        #     prize.achievement_prize_id = 'Mission_10019_211_1'
        #     prize.schema_key = 'ITEM'
        #     prize.value = b'{"Prefix":"Growth","Value":31015,"Count":10,"AchievementId":"Mission_10019_211"}'
        #     prize.system_resource_num = 1
        #     achievement.category = 'Mission'
        #     achievement.unlock = True

        #     inventory = response.inventories.add()
        #     inventory.id = '61ed4677-87dd-4f97-b937-49a872b0f7a5'
        #     inventory.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        #     inventory.schema_key = 'ITEM'
        #     inventory.value = b'{"Prefix":"Growth","Value":31015,"Count":10,"AchievementId":"Mission_10019_211"}'
        #     inventory.route = inventory.route.ACHIEVEMENT
        #     inventory.message = '期間限定ミッションの報酬です'
        #     inventory.search_label = 'Item'
        #     inventory.opened_at = 1665641192
        #     inventory.expired_at = 1668020400
        #     inventory.system_resource_num = 1
        #     inventory.created_at = 1665641192
        # if 'Mission_2_1_S0' in request.achievement_ids:
        #     player_achievement = response.player_achievements.add()
        #     achievement = player_achievement.achievement
        #     achievement.achievement_id = 'Mission_2_1_S0'
        #     achievement.value = b'{"Name":"Mission_2","Value":1}'
        #     achievement.opened_at = 1577804400
        #     achievement.closed_at = 4102412400
        #     achievement.reset_type = achievement.reset_type.DATE_LINE
        #     achievement.date_line = '04:00:00Z'
        #     prize = achievement.prizes.add()
        #     prize.achievement_id = 'Mission_2_1_S0'
        #     prize.achievement_prize_id = 'Mission_2_1_S0_1'
        #     prize.schema_key = 'ITEM'
        #     prize.value = b'{"Prefix":"Coin","Value":10001,"Count":1000,"AchievementId":"Mission_2_1_S0"}'
        #     prize.system_resource_num = 1
        #     achievement.category = 'Mission'
        #     achievement.unlock = True
        #     player_achievement.last_unlocked_at = 1665641192

        #     inventory = response.inventories.add()
        #     inventory.id = '97e4835f-1893-421f-87a4-209a82b42bef'
        #     inventory.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        #     inventory.schema_key = 'ITEM'
        #     inventory.value = b'{"Prefix":"Coin","Value":10001,"Count":1000,"AchievementId":"Mission_2_1_S0"}'
        #     inventory.route = inventory.route.ACHIEVEMENT
        #     inventory.message = 'デイリーミッションの報酬です'
        #     inventory.search_label = 'Coin'
        #     inventory.opened_at = 1665641192
        #     inventory.expired_at = 1668020400
        #     inventory.system_resource_num = 1
        #     inventory.created_at = 1665641192
        # if 'Mission_2_2_S0' in request.achievement_ids:
        #     player_achievement = response.player_achievements.add()
        #     achievement = player_achievement.achievement
        #     achievement.achievement_id = 'Mission_2_2_S0'
        #     achievement.value = b'{"Name":"Mission_2","Value":2}'
        #     achievement.opened_at = 1577804400
        #     achievement.closed_at = 4102412400
        #     achievement.reset_type = achievement.reset_type.DATE_LINE
        #     achievement.date_line = '04:00:00Z'
        #     prize = achievement.prizes.add()
        #     prize.achievement_id = 'Mission_2_2_S0'
        #     prize.achievement_prize_id = 'Mission_2_2_S0_1'
        #     prize.item_type = prize.item_type.PLAYER_KEY_VALUE_STORE
        #     prize.schema_key = 'PKVS'
        #     prize.value = b'{"Prefix":"PKVS","Value":60001,"Count":5,"AchievementId":"Mission_2_2_S0"}'
        #     prize.system_resource_name = 'point'
        #     prize.system_resource_num = 5
        #     achievement.category = 'Mission'
        #     achievement.unlock = True
        #     player_achievement.last_unlocked_at = 1665641192

        #     inventory = response.inventories.add()
        #     inventory.id = '3ab9c043-49ff-4e3b-99f8-f9fa956c5ac0'
        #     inventory.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        #     inventory.item_type = inventory.item_type.PLAYER_KEY_VALUE_STORE
        #     inventory.schema_key = 'PKVS'
        #     inventory.value = b'{"Prefix":"PKVS","Value":60001,"Count":5,"AchievementId":"Mission_2_2_S0"}'
        #     inventory.route = inventory.route.ACHIEVEMENT
        #     inventory.message = 'デイリーミッションの報酬です'
        #     inventory.search_label = 'Other'
        #     inventory.opened_at = 1665641192
        #     inventory.expired_at = 1668020400
        #     inventory.system_resource_name = 'point'
        #     inventory.system_resource_num = 5
        #     inventory.created_at = 1665641192
        # if 'Mission_2_3_S0' in request.achievement_ids:
        #     player_achievement = response.player_achievements.add()
        #     achievement = player_achievement.achievement
        #     achievement.achievement_id = 'Mission_2_3_S0'
        #     achievement.value = b'{"Name":"Mission_2","Value":3}'
        #     achievement.opened_at = 1577804400
        #     achievement.closed_at = 4102412400
        #     achievement.reset_type = achievement.reset_type.DATE_LINE
        #     achievement.date_line = '04:00:00Z'
        #     prize = achievement.prizes.add()
        #     prize.achievement_id = 'Mission_2_3_S0'
        #     prize.achievement_prize_id = 'Mission_2_3_S0_1'
        #     prize.schema_key = 'ITEM'
        #     prize.value = b'{"Prefix":"Growth","Value":30003,"Count":5,"AchievementId":"Mission_2_3_S0"}'
        #     prize.system_resource_num = 1
        #     achievement.category = 'Mission'
        #     achievement.unlock = True
        #     player_achievement.last_unlocked_at = 1665641192

        #     inventory = response.inventories.add()
        #     inventory.id = 'd4fcee47-cf38-446d-8465-4d5f63b9f31b'
        #     inventory.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        #     inventory.schema_key = 'ITEM'
        #     inventory.value = b'{"Prefix":"Growth","Value":30003,"Count":5,"AchievementId":"Mission_2_3_S0"}'
        #     inventory.route = inventory.route.ACHIEVEMENT
        #     inventory.message = 'デイリーミッションの報酬です'
        #     inventory.search_label = 'Item'
        #     inventory.opened_at = 1665641192
        #     inventory.expired_at = 1668020400
        #     inventory.system_resource_num = 1
        #     inventory.created_at = 1665641192
        # response.entries.extend(request.entries)
        for entry in response.entries:
            entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
            entry.created_at = int(time.time())
            entry.updated_at = int(time.time())
        response.revision = request.next_revision
        shared_storage.revision = request.next_revision
        return response


def add_AchievementServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: achievement_pb2.AchievementGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(achievement_pb2.AchievementGetAvailableV1.Response.SerializeToString(x)),
        ),
        'GetAvailableByIDsV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableByIDsV1,
            request_deserializer=lambda x: achievement_pb2.AchievementGetAvailableByIDsV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(achievement_pb2.AchievementGetAvailableByIDsV1.Response.SerializeToString(x)),
        ),
        'UnlockV1': grpc.unary_unary_rpc_method_handler(
            servicer.UnlockV1,
            request_deserializer=lambda x: achievement_pb2.AchievementUnlockV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(achievement_pb2.AchievementUnlockV1.Response.SerializeToString(x)),
        ),
        'UnlockAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.UnlockAndSavePlayerStorageV1,
            request_deserializer=lambda x: achievement_pb2.AchievementUnlockAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(achievement_pb2.AchievementUnlockAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.Achievement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

