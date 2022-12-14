from pathlib import Path
import time

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import player_key_value_store_pb2
from takasho.schema.common_featureset.player_api import player_key_value_store_pb2_grpc
from takasho.shared_storage import shared_storage


class PlayerKeyValueStore(player_key_value_store_pb2_grpc.PlayerKeyValueStoreServicer):

    def IncrementPlayerKeyValuesAndSavePlayerStorageV1(self, request, context):
        response = player_key_value_store_pb2.PlayerKeyValueStoreIncrementPlayerKeyValuesAndSavePlayerStorageV1.Response()
        for key in [v.key for v in request.player_key_values]:
            player_key_value = response.player_key_values.add()
            player_key_value.key = key
            player_key_value.value = 43607
            player_key_value.expired_at = 4102412400
        response.entries.extend(request.entries)
        for entry in response.entries:
            entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
            entry.created_at = int(time.time())
            entry.updated_at = int(time.time())
        response.revision = request.next_revision
        shared_storage.revision = request.next_revision
        return response


def add_PlayerKeyValueStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetPlayerKeyValuesV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetPlayerKeyValuesV1,
            request_deserializer=lambda x: player_key_value_store_pb2.PlayerKeyValueStoreGetPlayerKeyValuesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_key_value_store_pb2.PlayerKeyValueStoreGetPlayerKeyValuesV1.Response.SerializeToString(x)),
        ),
        'IncrementPlayerKeyValuesV1': grpc.unary_unary_rpc_method_handler(
            servicer.IncrementPlayerKeyValuesV1,
            request_deserializer=lambda x: player_key_value_store_pb2.PlayerKeyValueStoreIncrementPlayerKeyValuesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_key_value_store_pb2.PlayerKeyValueStoreIncrementPlayerKeyValuesV1.Response.SerializeToString(x)),
        ),
        'IncrementPlayerKeyValuesAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.IncrementPlayerKeyValuesAndSavePlayerStorageV1,
            request_deserializer=lambda x: player_key_value_store_pb2.PlayerKeyValueStoreIncrementPlayerKeyValuesAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_key_value_store_pb2.PlayerKeyValueStoreIncrementPlayerKeyValuesAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
        'UpdatePlayerKeyValuesAndSavePlayerStorageV1': grpc.unary_unary_rpc_method_handler(
            servicer.UpdatePlayerKeyValuesAndSavePlayerStorageV1,
            request_deserializer=lambda x: player_key_value_store_pb2.PlayerKeyValueStoreUpdatePlayerKeyValuesAndSavePlayerStorageV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_key_value_store_pb2.PlayerKeyValueStoreUpdatePlayerKeyValuesAndSavePlayerStorageV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.PlayerKeyValueStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

