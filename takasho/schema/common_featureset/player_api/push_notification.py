import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import push_notification_pb2
from takasho.schema.common_featureset.player_api import push_notification_pb2_grpc


class PushNotification(push_notification_pb2_grpc.PushNotificationServicer):
    
    def GetConfigV2(self, request, context):
        response = push_notification_pb2.PushNotificationGetConfigV2.Response()
        response.topic_ids.extend([
            'jp_release_i_remote_optin',
            'jp_release_night',
            'jp_release_i_night_optin'
        ])
        return response


def add_PushNotificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SetConfigV1': grpc.unary_unary_rpc_method_handler(
            servicer.SetConfigV1,
            request_deserializer=lambda x: push_notification_pb2.PushNotificationSetConfigV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(push_notification_pb2.PushNotificationSetConfigV1.Response.SerializeToString(x)),
        ),
        'SetConfigV2': grpc.unary_unary_rpc_method_handler(
            servicer.SetConfigV2,
            request_deserializer=lambda x: push_notification_pb2.PushNotificationSetConfigV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(push_notification_pb2.PushNotificationSetConfigV2.Response.SerializeToString(x)),
        ),
        'GetConfigV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetConfigV1,
            request_deserializer=lambda x: push_notification_pb2.PushNotificationGetConfigV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(push_notification_pb2.PushNotificationGetConfigV1.Response.SerializeToString(x)),
        ),
        'GetConfigV2': grpc.unary_unary_rpc_method_handler(
            servicer.GetConfigV2,
            request_deserializer=lambda x: push_notification_pb2.PushNotificationGetConfigV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(push_notification_pb2.PushNotificationGetConfigV2.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.PushNotification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

