import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import score_ranking_pb2
from takasho.schema.fes.player_api import score_ranking_pb2_grpc


class ScoreRanking(score_ranking_pb2_grpc.ScoreRankingServicer):
    
    def ReceiveClassPrizeV1(self, request, context):
        response = score_ranking_pb2.ScoreRankingReceiveClassPrizeV1.Response()
        return response


def add_ScoreRankingServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetAvailableV1.Response.SerializeToString(x)),
        ),
        'GetGrandPrixLeaderBoardV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetGrandPrixLeaderBoardV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Response.SerializeToString(x)),
        ),
        'GetClassGroupLeaderBoardV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetClassGroupLeaderBoardV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetClassGroupLeaderBoardV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetClassGroupLeaderBoardV1.Response.SerializeToString(x)),
        ),
        'GetGrandPrixRankV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetGrandPrixRankV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetGrandPrixRankV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetGrandPrixRankV1.Response.SerializeToString(x)),
        ),
        'GetClassGroupRankV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetClassGroupRankV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetClassGroupRankV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetClassGroupRankV1.Response.SerializeToString(x)),
        ),
        'GetClassV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetClassV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetClassV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetClassV1.Response.SerializeToString(x)),
        ),
        'RegisterV1': grpc.unary_unary_rpc_method_handler(
            servicer.RegisterV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingRegisterV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingRegisterV1.Response.SerializeToString(x)),
        ),
        'ReceiveClassPrizeV1': grpc.unary_unary_rpc_method_handler(
            servicer.ReceiveClassPrizeV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingReceiveClassPrizeV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingReceiveClassPrizeV1.Response.SerializeToString(x)),
        ),
        'ReceiveGrandPrixPrizeV1': grpc.unary_unary_rpc_method_handler(
            servicer.ReceiveGrandPrixPrizeV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingReceiveGrandPrixPrizeV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingReceiveGrandPrixPrizeV1.Response.SerializeToString(x)),
        ),
        'EntryV1': grpc.unary_unary_rpc_method_handler(
            servicer.EntryV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingEntryV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingEntryV1.Response.SerializeToString(x)),
        ),
        'GetClassGroupElevatingRankV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetClassGroupElevatingRankV1,
            request_deserializer=lambda x: score_ranking_pb2.ScoreRankingGetClassGroupElevatingRankV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(score_ranking_pb2.ScoreRankingGetClassGroupElevatingRankV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.ScoreRanking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

