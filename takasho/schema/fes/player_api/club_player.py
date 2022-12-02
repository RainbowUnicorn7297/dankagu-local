import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import club_player_pb2
from takasho.schema.fes.player_api import club_player_pb2_grpc


class ClubPlayer(club_player_pb2_grpc.ClubPlayerServicer):
    
    def GetClubs(self, request, context):
        response = club_player_pb2.ClubPlayerGetClubs.Response()
        return response


def add_ClubPlayerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetClubs': grpc.unary_unary_rpc_method_handler(
            servicer.GetClubs,
            request_deserializer=lambda x: club_player_pb2.ClubPlayerGetClubs.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_player_pb2.ClubPlayerGetClubs.Response.SerializeToString(x)),
        ),
        'GetPlayers': grpc.unary_unary_rpc_method_handler(
            servicer.GetPlayers,
            request_deserializer=lambda x: club_player_pb2.ClubPlayerGetPlayers.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_player_pb2.ClubPlayerGetPlayers.Response.SerializeToString(x)),
        ),
        'GetPlayersCount': grpc.unary_unary_rpc_method_handler(
            servicer.GetPlayersCount,
            request_deserializer=lambda x: club_player_pb2.ClubPlayerGetPlayersCount.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_player_pb2.ClubPlayerGetPlayersCount.Response.SerializeToString(x)),
        ),
        'KickPlayer': grpc.unary_unary_rpc_method_handler(
            servicer.KickPlayer,
            request_deserializer=lambda x: club_player_pb2.ClubPlayerKickPlayer.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_player_pb2.ClubPlayerKickPlayer.Response.SerializeToString(x)),
        ),
        'Leave': grpc.unary_unary_rpc_method_handler(
            servicer.Leave,
            request_deserializer=lambda x: club_player_pb2.ClubPlayerLeave.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_player_pb2.ClubPlayerLeave.Response.SerializeToString(x)),
        ),
        'UpdateRole': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateRole,
            request_deserializer=lambda x: club_player_pb2.ClubPlayerUpdateRole.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_player_pb2.ClubPlayerUpdateRole.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.club_player.ClubPlayer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

