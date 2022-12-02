# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.fes.player_api import reconstruction_spot_pb2 as takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2


class ReconstructionSpotStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAvailableV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ReconstructionSpot/GetAvailableV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotGetAvailableV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotGetAvailableV1.Response.FromString,
                )
        self.ReceivePrizesV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.ReconstructionSpot/ReceivePrizesV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotReceivePrizesV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotReceivePrizesV1.Response.FromString,
                )


class ReconstructionSpotServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAvailableV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceivePrizesV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReconstructionSpotServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAvailableV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotGetAvailableV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotGetAvailableV1.Response.SerializeToString,
            ),
            'ReceivePrizesV1': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceivePrizesV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotReceivePrizesV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotReceivePrizesV1.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.fes.player_api.ReconstructionSpot', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReconstructionSpot(object):
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
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ReconstructionSpot/GetAvailableV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotGetAvailableV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotGetAvailableV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceivePrizesV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.ReconstructionSpot/ReceivePrizesV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotReceivePrizesV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_reconstruction__spot__pb2.ReconstructionSpotReceivePrizesV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)