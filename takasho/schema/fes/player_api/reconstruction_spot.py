from pathlib import Path

import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import reconstruction_spot_pb2
from takasho.schema.fes.player_api import reconstruction_spot_pb2_grpc


class ReconstructionSpot(reconstruction_spot_pb2_grpc.ReconstructionSpotServicer):
    
    def GetAvailableV1(self, request, context):
        p = Path(__file__).with_name('reconstruction_spot.hex')
        with p.open() as f:
            response = reconstruction_spot_pb2. \
                ReconstructionSpotGetAvailableV1.Response.FromString(
                    bytes.fromhex(f.read()))
        return response
    
    def ReceivePrizesV1(self, request, context):
        response = reconstruction_spot_pb2.ReconstructionSpotReceivePrizesV1.Response()
        return response


def add_ReconstructionSpotServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: reconstruction_spot_pb2.ReconstructionSpotGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(reconstruction_spot_pb2.ReconstructionSpotGetAvailableV1.Response.SerializeToString(x)),
        ),
        'ReceivePrizesV1': grpc.unary_unary_rpc_method_handler(
            servicer.ReceivePrizesV1,
            request_deserializer=lambda x: reconstruction_spot_pb2.ReconstructionSpotReceivePrizesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(reconstruction_spot_pb2.ReconstructionSpotReceivePrizesV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.ReconstructionSpot', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

