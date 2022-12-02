import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import step_up_loot_box_pb2
from takasho.schema.common_featureset.player_api import step_up_loot_box_pb2_grpc


class StepUpLootBox(step_up_loot_box_pb2_grpc.StepUpLootBoxServicer):
    
    def GetAvailableV1(self, request, context):
        response = step_up_loot_box_pb2.StepUpLootBoxV2GetAvailableV1.Response()
        return response


def add_StepUpLootBoxServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxGetAvailableV1.Response.SerializeToString(x)),
        ),
        'PurchaseV1': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxPurchaseV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxPurchaseV1.Response.SerializeToString(x)),
        ),
        'GetProbabilityV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetProbabilityV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxGetProbabilityV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxGetProbabilityV1.Response.SerializeToString(x)),
        ),
        'GetDetailV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetDetailV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxGetDetailV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxGetDetailV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.StepUpLootBox', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

