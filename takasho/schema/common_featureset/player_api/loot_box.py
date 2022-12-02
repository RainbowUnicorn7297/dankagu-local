from pathlib import Path

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import loot_box_pb2
from takasho.schema.common_featureset.player_api import loot_box_pb2_grpc


class LootBox(loot_box_pb2_grpc.LootBoxServicer):
    
    def GetAvailableV1(self, request, context):
        response = loot_box_pb2.LootBoxV3GetAvailableV1.Response()
        if request.exclude_pickup_response:
            if request.page_token is None:
                p = Path(__file__).with_name('loot_box.hex')
            else:
                p = Path(__file__).with_name('loot_box.' + request.page_token + '.hex')
            with p.open() as f:
                response = loot_box_pb2.LootBoxV3GetAvailableV1.Response. \
                    FromString(bytes.fromhex(f.read()))
        return response


def add_LootBoxServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: loot_box_pb2.LootBoxGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(loot_box_pb2.LootBoxGetAvailableV1.Response.SerializeToString(x)),
        ),
        'PurchaseV1': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseV1,
            request_deserializer=lambda x: loot_box_pb2.LootBoxPurchaseV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(loot_box_pb2.LootBoxPurchaseV1.Response.SerializeToString(x)),
        ),
        'GetProbabilityV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetProbabilityV1,
            request_deserializer=lambda x: loot_box_pb2.LootBoxGetProbabilityV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(loot_box_pb2.LootBoxGetProbabilityV1.Response.SerializeToString(x)),
        ),
        'GetDetailV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetDetailV1,
            request_deserializer=lambda x: loot_box_pb2.LootBoxGetDetailV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(loot_box_pb2.LootBoxGetDetailV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.LootBox', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

