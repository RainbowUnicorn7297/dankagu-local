import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import club_achievement_pb2
from takasho.schema.fes.player_api import club_achievement_pb2_grpc


class ClubAchievement(club_achievement_pb2_grpc.ClubAchievementServicer):
    
    def UnlockAndIncrementClubScalar(self, request, context):
        response = club_achievement_pb2.ClubAchievementUnlockAndIncrementClubScalar.Response()
        return response


def add_ClubAchievementServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailable': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailable,
            request_deserializer=lambda x: club_achievement_pb2.ClubAchievementGetAvailable.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_achievement_pb2.ClubAchievementGetAvailable.Response.SerializeToString(x)),
        ),
        'UnlockAndIncrementClubScalar': grpc.unary_unary_rpc_method_handler(
            servicer.UnlockAndIncrementClubScalar,
            request_deserializer=lambda x: club_achievement_pb2.ClubAchievementUnlockAndIncrementClubScalar.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_achievement_pb2.ClubAchievementUnlockAndIncrementClubScalar.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.club_achievement.ClubAchievement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

