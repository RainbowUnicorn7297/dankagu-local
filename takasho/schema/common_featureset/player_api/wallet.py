from pathlib import Path

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import wallet_pb2
from takasho.schema.common_featureset.player_api import wallet_pb2_grpc


class Wallet(wallet_pb2_grpc.WalletServicer):
    
    def GetBalancesV2(self, request, context):
        response = wallet_pb2.WalletGetBalancesV2.Response()
        p = Path(__file__).with_name('wallet.hex')
        with p.open() as f:
            r = wallet_pb2.WalletGetBalancesV2.Response.FromString(
                bytes.fromhex(f.read()))
        response.total.CopyFrom(r.total)
        response.expiration.CopyFrom(r.expiration)
        response.expired_at = request.expired_at
        return response


def add_WalletServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetBalancesV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetBalancesV1,
            request_deserializer=lambda x: wallet_pb2.WalletGetBalancesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(wallet_pb2.WalletGetBalancesV1.Response.SerializeToString(x)),
        ),
        'GetBalancesV2': grpc.unary_unary_rpc_method_handler(
            servicer.GetBalancesV2,
            request_deserializer=lambda x: wallet_pb2.WalletGetBalancesV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(wallet_pb2.WalletGetBalancesV2.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.Wallet', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

