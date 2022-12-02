# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.common_featureset.player_api import push_notification_pb2 as takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2


class PushNotificationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetConfigV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.PushNotification/SetConfigV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV1.Response.FromString,
                )
        self.SetConfigV2 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.PushNotification/SetConfigV2',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV2.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV2.Response.FromString,
                )
        self.GetConfigV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.PushNotification/GetConfigV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV1.Response.FromString,
                )
        self.GetConfigV2 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.PushNotification/GetConfigV2',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV2.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV2.Response.FromString,
                )


class PushNotificationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetConfigV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfigV2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfigV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfigV2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PushNotificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetConfigV1': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV1.Response.SerializeToString,
            ),
            'SetConfigV2': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfigV2,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV2.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV2.Response.SerializeToString,
            ),
            'GetConfigV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfigV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV1.Response.SerializeToString,
            ),
            'GetConfigV2': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfigV2,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV2.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.common_featureset.player_api.PushNotification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PushNotification(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetConfigV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.PushNotification/SetConfigV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV1.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfigV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.PushNotification/SetConfigV2',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV2.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationSetConfigV2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfigV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.PushNotification/GetConfigV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV1.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfigV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.PushNotification/GetConfigV2',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV2.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_push__notification__pb2.PushNotificationGetConfigV2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)