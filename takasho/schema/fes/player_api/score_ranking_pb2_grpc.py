# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.fes.player_api import score_ranking_pb2 as takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2


class ScoreRankingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAvailableV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetAvailableV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetAvailableV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetAvailableV1.Response.FromString,
                )
        self.GetGrandPrixLeaderBoardV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetGrandPrixLeaderBoardV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Response.FromString,
                )
        self.GetClassGroupLeaderBoardV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetClassGroupLeaderBoardV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupLeaderBoardV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupLeaderBoardV1.Response.FromString,
                )
        self.GetGrandPrixRankV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetGrandPrixRankV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixRankV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixRankV1.Response.FromString,
                )
        self.GetClassGroupRankV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetClassGroupRankV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupRankV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupRankV1.Response.FromString,
                )
        self.GetClassV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetClassV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassV1.Response.FromString,
                )
        self.RegisterV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/RegisterV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingRegisterV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingRegisterV1.Response.FromString,
                )
        self.ReceiveClassPrizeV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/ReceiveClassPrizeV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveClassPrizeV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveClassPrizeV1.Response.FromString,
                )
        self.ReceiveGrandPrixPrizeV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/ReceiveGrandPrixPrizeV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveGrandPrixPrizeV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveGrandPrixPrizeV1.Response.FromString,
                )
        self.EntryV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/EntryV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingEntryV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingEntryV1.Response.FromString,
                )
        self.GetClassGroupElevatingRankV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ScoreRanking/GetClassGroupElevatingRankV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupElevatingRankV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupElevatingRankV1.Response.FromString,
                )


class ScoreRankingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAvailableV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGrandPrixLeaderBoardV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClassGroupLeaderBoardV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGrandPrixRankV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClassGroupRankV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClassV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveClassPrizeV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveGrandPrixPrizeV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EntryV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClassGroupElevatingRankV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScoreRankingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAvailableV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetAvailableV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetAvailableV1.Response.SerializeToString,
            ),
            'GetGrandPrixLeaderBoardV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGrandPrixLeaderBoardV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Response.SerializeToString,
            ),
            'GetClassGroupLeaderBoardV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClassGroupLeaderBoardV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupLeaderBoardV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupLeaderBoardV1.Response.SerializeToString,
            ),
            'GetGrandPrixRankV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGrandPrixRankV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixRankV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixRankV1.Response.SerializeToString,
            ),
            'GetClassGroupRankV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClassGroupRankV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupRankV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupRankV1.Response.SerializeToString,
            ),
            'GetClassV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClassV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassV1.Response.SerializeToString,
            ),
            'RegisterV1': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingRegisterV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingRegisterV1.Response.SerializeToString,
            ),
            'ReceiveClassPrizeV1': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveClassPrizeV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveClassPrizeV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveClassPrizeV1.Response.SerializeToString,
            ),
            'ReceiveGrandPrixPrizeV1': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveGrandPrixPrizeV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveGrandPrixPrizeV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveGrandPrixPrizeV1.Response.SerializeToString,
            ),
            'EntryV1': grpc.unary_unary_rpc_method_handler(
                    servicer.EntryV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingEntryV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingEntryV1.Response.SerializeToString,
            ),
            'GetClassGroupElevatingRankV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClassGroupElevatingRankV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupElevatingRankV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupElevatingRankV1.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.fes.player_api.ScoreRanking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScoreRanking(object):
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
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetAvailableV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetAvailableV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetAvailableV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGrandPrixLeaderBoardV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetGrandPrixLeaderBoardV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixLeaderBoardV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClassGroupLeaderBoardV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetClassGroupLeaderBoardV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupLeaderBoardV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupLeaderBoardV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGrandPrixRankV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetGrandPrixRankV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixRankV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetGrandPrixRankV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClassGroupRankV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetClassGroupRankV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupRankV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupRankV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClassV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetClassV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/RegisterV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingRegisterV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingRegisterV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveClassPrizeV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/ReceiveClassPrizeV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveClassPrizeV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveClassPrizeV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveGrandPrixPrizeV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/ReceiveGrandPrixPrizeV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveGrandPrixPrizeV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingReceiveGrandPrixPrizeV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EntryV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/EntryV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingEntryV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingEntryV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClassGroupElevatingRankV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ScoreRanking/GetClassGroupElevatingRankV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupElevatingRankV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_score__ranking__pb2.ScoreRankingGetClassGroupElevatingRankV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)