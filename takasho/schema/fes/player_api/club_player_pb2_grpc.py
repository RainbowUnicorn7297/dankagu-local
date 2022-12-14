# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.fes.player_api import club_player_pb2 as takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2


class ClubPlayerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetClubs = channel.unary_unary(
                '/takasho.schema.fes.player_api.club_player.ClubPlayer/GetClubs',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetClubs.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetClubs.Response.FromString,
                )
        self.GetPlayers = channel.unary_unary(
                '/takasho.schema.fes.player_api.club_player.ClubPlayer/GetPlayers',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayers.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayers.Response.FromString,
                )
        self.GetPlayersCount = channel.unary_unary(
                '/takasho.schema.fes.player_api.club_player.ClubPlayer/GetPlayersCount',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayersCount.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayersCount.Response.FromString,
                )
        self.KickPlayer = channel.unary_unary(
                '/takasho.schema.fes.player_api.club_player.ClubPlayer/KickPlayer',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerKickPlayer.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerKickPlayer.Response.FromString,
                )
        self.Leave = channel.unary_unary(
                '/takasho.schema.fes.player_api.club_player.ClubPlayer/Leave',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerLeave.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerLeave.Response.FromString,
                )
        self.UpdateRole = channel.unary_unary(
                '/takasho.schema.fes.player_api.club_player.ClubPlayer/UpdateRole',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerUpdateRole.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerUpdateRole.Response.FromString,
                )


class ClubPlayerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetClubs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayersCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KickPlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Leave(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClubPlayerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetClubs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClubs,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetClubs.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetClubs.Response.SerializeToString,
            ),
            'GetPlayers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayers,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayers.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayers.Response.SerializeToString,
            ),
            'GetPlayersCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayersCount,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayersCount.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayersCount.Response.SerializeToString,
            ),
            'KickPlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.KickPlayer,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerKickPlayer.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerKickPlayer.Response.SerializeToString,
            ),
            'Leave': grpc.unary_unary_rpc_method_handler(
                    servicer.Leave,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerLeave.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerLeave.Response.SerializeToString,
            ),
            'UpdateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRole,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerUpdateRole.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerUpdateRole.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.fes.player_api.club_player.ClubPlayer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClubPlayer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetClubs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.club_player.ClubPlayer/GetClubs',
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetClubs.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetClubs.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.club_player.ClubPlayer/GetPlayers',
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayers.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayers.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayersCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.club_player.ClubPlayer/GetPlayersCount',
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayersCount.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerGetPlayersCount.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KickPlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.club_player.ClubPlayer/KickPlayer',
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerKickPlayer.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerKickPlayer.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Leave(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.club_player.ClubPlayer/Leave',
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerLeave.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerLeave.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.club_player.ClubPlayer/UpdateRole',
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerUpdateRole.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_club__player__pb2.ClubPlayerUpdateRole.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
