import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import player_event_log_pb2
from takasho.schema.common_featureset.player_api import player_event_log_pb2_grpc


class PlayerEventLog(player_event_log_pb2_grpc.PlayerEventLogServicer):
    
    def SendV1(self, request, context):
        response = player_event_log_pb2.PlayerEventLogSendV1.Response()
        return response


def add_PlayerEventLogServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SendV1': grpc.unary_unary_rpc_method_handler(
            servicer.SendV1,
            request_deserializer=lambda x: player_event_log_pb2.PlayerEventLogSendV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_event_log_pb2.PlayerEventLogSendV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.PlayerEventLog', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

