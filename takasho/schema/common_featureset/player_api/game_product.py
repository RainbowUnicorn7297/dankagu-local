import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import game_product_pb2
from takasho.schema.common_featureset.player_api import game_product_pb2_grpc


class GameProduct(game_product_pb2_grpc.GameProductServicer):
    
    def GetAvailableV1(self, request, context):
        if request.page_token is None:
            filename = 'game_product.hex'
        else:
            filename = 'game_product.' + request.page_token + '.hex'
        with open (filename) as f:
            response = game_product_pb2.GameProductGetAvailableV1.Response. \
                FromString(bytes.fromhex(f.read()))
        return response


def add_GameProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: game_product_pb2.GameProductGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_product_pb2.GameProductGetAvailableV1.Response.SerializeToString(x)),
        ),
        'PurchaseV1': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseV1,
            request_deserializer=lambda x: game_product_pb2.GameProductPurchaseV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_product_pb2.GameProductPurchaseV1.Response.SerializeToString(x)),
        ),
        'PurchaseV2': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseV2,
            request_deserializer=lambda x: game_product_pb2.GameProductPurchaseV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_product_pb2.GameProductPurchaseV2.Response.SerializeToString(x)),
        ),
        'PurchaseAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseAndSavePlayerStorageV1,
            request_deserializer=lambda x: game_product_pb2.GameProductPurchaseAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_product_pb2.GameProductPurchaseAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
        'PurchaseAndSavePlayerStorageV2': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseAndSavePlayerStorageV2,
            request_deserializer=lambda x: game_product_pb2.GameProductPurchaseAndSavePlayerStorageV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(game_product_pb2.GameProductPurchaseAndSavePlayerStorageV2.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.GameProduct', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

