import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import step_up_loot_box_pb2
from takasho.schema.common_featureset.player_api import step_up_loot_box_pb2_grpc


class StepUpLootBoxV2(step_up_loot_box_pb2_grpc.StepUpLootBoxV2Servicer):
    
    def GetAvailableV1(self, request, context):
        response = step_up_loot_box_pb2.StepUpLootBoxV2GetAvailableV1.Response()
        return response


def add_StepUpLootBoxV2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxV2GetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxV2GetAvailableV1.Response.SerializeToString(x)),
        ),
        'PurchaseV1': grpc.unary_unary_rpc_method_handler(
            servicer.PurchaseV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxV2PurchaseV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxV2PurchaseV1.Response.SerializeToString(x)),
        ),
        'GetProbabilityV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetProbabilityV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxV2GetProbabilityV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxV2GetProbabilityV1.Response.SerializeToString(x)),
        ),
        'GetDetailV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetDetailV1,
            request_deserializer=lambda x: step_up_loot_box_pb2.StepUpLootBoxV2GetDetailV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(step_up_loot_box_pb2.StepUpLootBoxV2GetDetailV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.StepUpLootBoxV2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

