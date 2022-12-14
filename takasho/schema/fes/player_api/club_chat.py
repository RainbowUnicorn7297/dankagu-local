import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import club_chat_pb2
from takasho.schema.fes.player_api import club_chat_pb2_grpc


class ClubChat(club_chat_pb2_grpc.ClubChatServicer):
    
    def GetMessagesCount(self, request, context):
        response = club_chat_pb2.ClubChatGetMessagesCount.Response()
        return response


def add_ClubChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateMessage': grpc.unary_unary_rpc_method_handler(
            servicer.CreateMessage,
            request_deserializer=lambda x: club_chat_pb2.ClubChatCreateMessage.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_chat_pb2.ClubChatCreateMessage.Response.SerializeToString(x)),
        ),
        'Get': grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=lambda x: club_chat_pb2.ClubChatGet.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_chat_pb2.ClubChatGet.Response.SerializeToString(x)),
        ),
        'GetMessagesCount': grpc.unary_unary_rpc_method_handler(
            servicer.GetMessagesCount,
            request_deserializer=lambda x: club_chat_pb2.ClubChatGetMessagesCount.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(club_chat_pb2.ClubChatGetMessagesCount.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.club_chat.ClubChat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

