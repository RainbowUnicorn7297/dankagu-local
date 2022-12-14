import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import game_message_pb2
from takasho.schema.common_featureset.player_api import game_message_pb2_grpc


class GameMessage(game_message_pb2_grpc.GameMessageServicer):
    
    def GetMessageV1(self, request, context):
        response = game_message_pb2.GameMessageGetMessageV1.Response()
        return response


def add_GameMessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetUnreadMessageV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetUnreadMessageV1,
            request_deserializer=lambda x: game_message_pb2.GameMessageGetUnreadMessageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_message_pb2.GameMessageGetUnreadMessageV1.Response.SerializeToString(x)),
        ),
        'GetMessageV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetMessageV1,
            request_deserializer=lambda x: game_message_pb2.GameMessageGetMessageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_message_pb2.GameMessageGetMessageV1.Response.SerializeToString(x)),
        ),
        'ReceiveMessageV1': grpc.unary_unary_rpc_method_handler(
            servicer.ReceiveMessageV1,
            request_deserializer=lambda x: game_message_pb2.GameMessageReceiveMessageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_message_pb2.GameMessageReceiveMessageV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.GameMessage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

