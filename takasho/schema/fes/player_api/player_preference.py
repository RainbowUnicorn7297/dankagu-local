import time

import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import player_preference_pb2
from takasho.schema.fes.player_api import player_preference_pb2_grpc


class FesPlayerPreference(player_preference_pb2_grpc.FesPlayerPreferenceServicer):
    
    def GetV1(self, request, context):
        response = player_preference_pb2.FesPlayerPreferenceGetV1.Response()
        player_preference = response.player_preference
        player_preference.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        player_preference.player_level = 500
        player_preference.is_my_space_released = True
        return response
    
    def SetAndSavePlayerStorageV1(self, request, context):
        response = player_preference_pb2.FesPlayerPreferenceSetAndSavePlayerStorageV1.Response()
        response.player_preference.CopyFrom(request.player_preference)
        response.entries.extend(request.entries)
        for entry in response.entries:
            entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
            entry.created_at = int(time.time())
            entry.updated_at = int(time.time())
        response.revision = request.next_revision
        return response


def add_FesPlayerPreferenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetV1,
            request_deserializer=lambda x: player_preference_pb2.FesPlayerPreferenceGetV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.FesPlayerPreferenceGetV1.Response.SerializeToString(x)),
        ),
        'SetAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.SetAndSavePlayerStorageV1,
            request_deserializer=lambda x: player_preference_pb2.FesPlayerPreferenceSetAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_preference_pb2.FesPlayerPreferenceSetAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.player_preference.FesPlayerPreference', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

