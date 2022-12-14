import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import player_achievement_pb2
from takasho.schema.common_featureset.player_api import player_achievement_pb2_grpc


class PlayerAchievement(player_achievement_pb2_grpc.PlayerAchievementServicer):
    
    def GetAvailableV1(self, request, context):
        response = player_achievement_pb2.PlayerAchievementGetAvailableV1. \
            Response()
        # if request.criterion.category == 'AllUserPresent':
        #     player_achievement = response.player_achievements.add()
        #     achievement = player_achievement.achievement
        #     achievement.achievement_id = 'AllUserPresent_96'
        #     achievement.value = b'{"Name":"AllUserPresent","Value":96,"IsContainNewUser":0,"PresentType":3,"ClientVersion":"2.1.0","CreateAt":1665640800}'
        #     achievement.opened_at = 1665640800
        #     achievement.closed_at = 1666245600
        #     achievement.date_line = '04:00:00Z'
        #     prize = achievement.prizes.add()
        #     prize.achievement_id = 'AllUserPresent_96'
        #     prize.achievement_prize_id = 'AllUserPresent_96_1'
        #     prize.item_type = prize.item_type.VIRTUAL_CURRENCY
        #     prize.schema_key = 'VC'
        #     prize.value = b'{"ItemId":100090001,"Prefix":"VC","Value":90001,"Count":100,"AchievementId":"AllUserPresent_96","PresentType":3}'
        #     prize.system_resource_name = 'FREE_STONE'
        #     prize.system_resource_num = 100
        #     achievement.category = 'AllUserPresent'
        return response
    
    def UnlockV1(self, request, context):
        response = player_achievement_pb2.PlayerAchievementUnlockV1.Response()
        # if 'AllUserPresent_96' in request.achievement_ids:
        #     player_achievement = response.player_achievements.add()
        #     achievement = player_achievement.achievement
        #     achievement.achievement_id = 'AllUserPresent_96'
        #     achievement.value = b'{"Name":"AllUserPresent","Value":96,"IsContainNewUser":0,"PresentType":3,"ClientVersion":"2.1.0","CreateAt":1665640800}'
        #     achievement.opened_at = 1665640800
        #     achievement.closed_at = 1666245600
        #     achievement.date_line = '04:00:00Z'
        #     prize = achievement.prizes.add()
        #     prize.achievement_id = 'AllUserPresent_96'
        #     prize.achievement_prize_id = 'AllUserPresent_96_1'
        #     prize.item_type = prize.item_type.VIRTUAL_CURRENCY
        #     prize.schema_key = 'VC'
        #     prize.value = b'{"ItemId":100090001,"Prefix":"VC","Value":90001,"Count":100,"AchievementId":"AllUserPresent_96","PresentType":3}'
        #     prize.system_resource_name = 'FREE_STONE'
        #     prize.system_resource_num = 100
        #     achievement.category = 'AllUserPresent'
        #     achievement.unlock = True
        #     inventory = response.inventories.add()
        #     inventory.id = '1fbede23-97ab-4443-9fd9-d8e5091bf2b6'
        #     inventory.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        #     inventory.item_type = inventory.item_type.VIRTUAL_CURRENCY
        #     inventory.schema_key = 'VC'
        #     inventory.value = b'{"ItemId":100090001,"Prefix":"VC","Value":90001,"Count":100,"AchievementId":"AllUserPresent_96","PresentType":3}'
        #     inventory.route = inventory.route.ACHIEVEMENT
        #     inventory.message = '運営からのお詫び'
        #     inventory.search_label = 'VC'
        #     inventory.opened_at = 1665641144
        #     inventory.expired_at = 1668020400
        #     inventory.system_resource_name = 'FREE_STONE'
        #     inventory.system_resource_num = 100
        #     inventory.created_at = 1665641144
        return response


def add_PlayerAchievementServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: player_achievement_pb2.PlayerAchievementGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_achievement_pb2.PlayerAchievementGetAvailableV1.Response.SerializeToString(x)),
        ),
        'GetAvailableByIDsV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableByIDsV1,
            request_deserializer=lambda x: player_achievement_pb2.PlayerAchievementGetAvailableByIDsV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_achievement_pb2.PlayerAchievementGetAvailableByIDsV1.Response.SerializeToString(x)),
        ),
        'UnlockV1': grpc.unary_unary_rpc_method_handler(
            servicer.UnlockV1,
            request_deserializer=lambda x: player_achievement_pb2.PlayerAchievementUnlockV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_achievement_pb2.PlayerAchievementUnlockV1.Response.SerializeToString(x)),
        ),
        'UnlockAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.UnlockAndSavePlayerStorageV1,
            request_deserializer=lambda x: player_achievement_pb2.PlayerAchievementUnlockAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_achievement_pb2.PlayerAchievementUnlockAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.PlayerAchievement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

