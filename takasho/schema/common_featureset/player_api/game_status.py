import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import game_status_pb2
from takasho.schema.common_featureset.player_api import game_status_pb2_grpc


class GameStatus(game_status_pb2_grpc.GameStatusServicer):
    
    def GetV1(self, request, context):
        response = game_status_pb2.GameStatusGetV1.Response()
        for v in request.values:
            status = request.statuses.add()
            status.value = v.value
        return response


def add_GameStatusServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetV1,
            request_deserializer=lambda x: game_status_pb2.GameStatusGetV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_status_pb2.GameStatusGetV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.GameStatus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

