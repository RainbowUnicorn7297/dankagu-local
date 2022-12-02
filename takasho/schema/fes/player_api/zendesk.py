import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import zendesk_pb2
from takasho.schema.fes.player_api import zendesk_pb2_grpc


class Zendesk(zendesk_pb2_grpc.ZendeskServicer):

    def GetUnreadCountV1(self, request, context):
        response = zendesk_pb2.ZendeskGetUnreadCountV1.Response()
        return response


def add_ZendeskServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUnreadCountV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUnreadCountV1,
                    request_deserializer=lambda x: zendesk_pb2.ZendeskGetUnreadCountV1.Request.FromString(packer.unpack(x)),
                    response_serializer=lambda x: packer.pack(zendesk_pb2.ZendeskGetUnreadCountV1.Response.SerializeToString(x)),
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.fes.player_api.Zendesk', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

