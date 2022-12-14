# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.common_featureset.player_api import achievement_pb2 as takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2


class AchievementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAvailableV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.Achievement/GetAvailableV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableV1.Response.FromString,
                )
        self.GetAvailableByIDsV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.Achievement/GetAvailableByIDsV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableByIDsV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableByIDsV1.Response.FromString,
                )
        self.UnlockV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.Achievement/UnlockV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockV1.Response.FromString,
                )
        self.UnlockAndSavePlayerStorageV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.Achievement/UnlockAndSavePlayerStorageV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockAndSavePlayerStorageV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockAndSavePlayerStorageV1.Response.FromString,
                )


class AchievementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAvailableV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAvailableByIDsV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockAndSavePlayerStorageV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AchievementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAvailableV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableV1.Response.SerializeToString,
            ),
            'GetAvailableByIDsV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAvailableByIDsV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableByIDsV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableByIDsV1.Response.SerializeToString,
            ),
            'UnlockV1': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockV1.Response.SerializeToString,
            ),
            'UnlockAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockAndSavePlayerStorageV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockAndSavePlayerStorageV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockAndSavePlayerStorageV1.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.common_featureset.player_api.Achievement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Achievement(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAvailableV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.Achievement/GetAvailableV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableV1.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAvailableByIDsV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.Achievement/GetAvailableByIDsV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableByIDsV1.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementGetAvailableByIDsV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnlockV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.Achievement/UnlockV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockV1.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnlockAndSavePlayerStorageV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.Achievement/UnlockAndSavePlayerStorageV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockAndSavePlayerStorageV1.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_achievement__pb2.AchievementUnlockAndSavePlayerStorageV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
