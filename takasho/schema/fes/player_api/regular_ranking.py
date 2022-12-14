import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import regular_ranking_pb2
from takasho.schema.fes.player_api import regular_ranking_pb2_grpc


class RegularRanking(regular_ranking_pb2_grpc.RegularRankingServicer):
    
    def RegisterV1(self, request, context):
        response = regular_ranking_pb2.RegularRankingRegisterV1.Response()
        player_ranking = response.player_ranking
        player_ranking.ranking_key = request.ranking_key
        player_ranking.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        player_ranking.nick_name = 'DanKagu'
        player_ranking.score = request.score
        return response


def add_RegularRankingServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'RegisterV1': grpc.unary_unary_rpc_method_handler(
            servicer.RegisterV1,
            request_deserializer=lambda x: regular_ranking_pb2.RegularRankingRegisterV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(regular_ranking_pb2.RegularRankingRegisterV1.Response.SerializeToString(x)),
        ),
        'GetTopRankingV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetTopRankingV1,
            request_deserializer=lambda x: regular_ranking_pb2.RegularRankingGetTopRankingV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(regular_ranking_pb2.RegularRankingGetTopRankingV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.RegularRanking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

