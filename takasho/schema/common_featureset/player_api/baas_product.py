import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import baas_product_pb2
from takasho.schema.common_featureset.player_api import baas_product_pb2_grpc


class BaasProduct(baas_product_pb2_grpc.BaasProductServicer):
    
    def GetAvailableByIDsV1(self, request, context):
        response = baas_product_pb2.BaasProductGetAvailableByIDsV1.Response()
        if 'com.dena.game.12026801.kagurapass1_tier8' in request.product_ids:
            baas_product = response.baas_products.add()
            baas_product.baas_product_id = 'com.dena.game.12026801.kagurapass1_tier8'
            baas_product.inventory_message = 'ゴールドカグラパス'
            extra = baas_product.extras.add()
            extra.baas_product_extra_id = 'com.dena.game.12026801.kagurapass1_tier8'
            extra.schema_key = 'ITEM'
            extra.value = b'{"ItemId":2900000002,"Prefix":"DanmakuPassActivationKey","Value":2,"Count":1,"BassPrdouctId":"kagurapass1_tier8","Extra":"\343\201\212\343\201\276\343\201\221"}'
            extra.system_resource_num = 1
            extra.search_label = 'ActivationKey'
        if 'com.dena.game.12026801.kagurapass2_tier24' in request.product_ids:
            baas_product = response.baas_products.add()
            baas_product.baas_product_id = 'com.dena.game.12026801.kagurapass2_tier24'
            baas_product.inventory_message = 'プラチナカグラパス'
            extra = baas_product.extras.add()
            extra.baas_product_extra_id = 'com.dena.game.12026801.kagurapass2_tier24'
            extra.schema_key = 'ITEM'
            extra.value = b'{"ItemId":2900000003,"Prefix":"DanmakuPassActivationKey","Value":3,"Count":1,"BassPrdouctId":"kagurapass2_tier24","Extra":"\343\201\212\343\201\276\343\201\221"}'
            extra.system_resource_num = 1
            extra.search_label = 'ActivationKey'
        return response


def add_BaasProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableByIDsV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableByIDsV1,
            request_deserializer=lambda x: baas_product_pb2.BaasProductGetAvailableByIDsV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(baas_product_pb2.BaasProductGetAvailableByIDsV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.BaasProduct', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

