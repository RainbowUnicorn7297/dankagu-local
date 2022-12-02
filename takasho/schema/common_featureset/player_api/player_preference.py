import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import player_preference_pb2
from takasho.schema.common_featureset.player_api import player_preference_pb2_grpc


class PlayerPreference(player_preference_pb2_grpc.PlayerPreferenceServicer):
    
    def GetPreferenceV1(self, request, context):
        response = player_preference_pb2.PlayerPreferenceGetPreferenceV1.Response()
        preference = response.preference
        preference.birth_year = 2021
        preference.birth_month = 8
        preference.consented_tos_version = 'v1'
        preference.created_at = 1628074800
        preference.updated_at = 1666954800
        preference.nickname = 'DanKagu'
        preference.nickname_updated_at = -62135596800
        preference.max_friend_number = -1
        preference.max_friend_request_queue_length = -1
        response.player_short_id = '00000000'
        return response
    
    def GetMonthlyBillingLimitV1(self, request, context):
        response = player_preference_pb2.PlayerPreferenceGetMonthlyBillingLimitV1.Response()
        return response


def add_PlayerPreferenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetPreferenceV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetPreferenceV1,
            request_deserializer=lambda x: player_preference_pb2.PlayerPreferenceGetPreferenceV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.PlayerPreferenceGetPreferenceV1.Response.SerializeToString(x)),
        ),
        'SetPreferenceV1': grpc.unary_unary_rpc_method_handler(
            servicer.SetPreferenceV1,
            request_deserializer=lambda x: player_preference_pb2.PlayerPreferenceSetPreferenceV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.PlayerPreferenceSetPreferenceV1.Response.SerializeToString(x)),
        ),
        'SetPreferenceAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.SetPreferenceAndSavePlayerStorageV1,
            request_deserializer=lambda x: player_preference_pb2.PlayerPreferenceSetPreferenceAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.PlayerPreferenceSetPreferenceAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
        'GetMonthlyBillingLimitV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetMonthlyBillingLimitV1,
            request_deserializer=lambda x: player_preference_pb2.PlayerPreferenceGetMonthlyBillingLimitV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.PlayerPreferenceGetMonthlyBillingLimitV1.Response.SerializeToString(x)),
        ),
        'GetMonthlyPurchaseSummaryV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetMonthlyPurchaseSummaryV1,
            request_deserializer=lambda x: player_preference_pb2.PlayerPreferenceGetMonthlyPurchaseSummaryV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.PlayerPreferenceGetMonthlyPurchaseSummaryV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.PlayerPreference', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

