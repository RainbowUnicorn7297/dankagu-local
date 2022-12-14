from pathlib import Path
import time

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import player_inventory_pb2
from takasho.schema.common_featureset.player_api import player_inventory_pb2_grpc
from takasho.schema.common_featureset.player_api import wallet_pb2
from takasho.shared_storage import shared_storage


class PlayerInventory(player_inventory_pb2_grpc.PlayerInventoryServicer):
    
    def GetInventoriesV1(self, request, context):
        response = player_inventory_pb2.PlayerInventoryGetInventoriesV1.Response()
        search_labels = request.criterion.search_labels
        if 'Exchange' in search_labels:
            pass
        elif 'AdPoint' in search_labels:
            pass
        elif 'ActivationKey' in search_labels:
            pass
        elif 'CoopProgressItem' in search_labels:
            pass
        elif '' in search_labels:
            pass
        elif 'VC' in search_labels:
            pass
        elif 'Card' in search_labels:
            pass
        elif 'Item' in search_labels:
            pass
        elif 'Coin' in search_labels:
            pass
        elif 'SelectTicket' in search_labels:
            pass
        elif 'GachaTicket' in search_labels:
            pass
        elif 'Other' in search_labels:
            pass
        elif 'NoFilter' in search_labels:
            pass
        return response
    
    def ReceiveV1(self, request, context):
        response = player_inventory_pb2.PlayerInventoryReceiveV1.Response()
        response.entries.extend(request.entries)
        for entry in response.entries:
            entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
            entry.created_at = int(time.time())
            entry.updated_at = int(time.time())
        response.revision = request.next_revision
        shared_storage.revision = request.next_revision
        p = Path(__file__).with_name('wallet.hex')
        with p.open() as f:
            total = wallet_pb2.WalletGetBalancesV2.Response.FromString(
                bytes.fromhex(f.read())).total
        response.wallet.CopyFrom(total)
        player_key_value = response.player_key_values.add()
        player_key_value.key = 'point'
        player_key_value.amount = 8622
        return response


def add_PlayerInventoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetInventoriesV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetInventoriesV1,
            request_deserializer=lambda x: player_inventory_pb2.PlayerInventoryGetInventoriesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_inventory_pb2.PlayerInventoryGetInventoriesV1.Response.SerializeToString(x)),
        ),
        'GetReceivedInventoriesV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetReceivedInventoriesV1,
            request_deserializer=lambda x: player_inventory_pb2.PlayerInventoryGetReceivedInventoriesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_inventory_pb2.PlayerInventoryGetReceivedInventoriesV1.Response.SerializeToString(x)),
        ),
        'ReceiveV1': grpc.unary_unary_rpc_method_handler(
            servicer.ReceiveV1,
            request_deserializer=lambda x: player_inventory_pb2.PlayerInventoryReceiveV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_inventory_pb2.PlayerInventoryReceiveV1.Response.SerializeToString(x)),
        ),
        'GetInventoriesAndCountV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetInventoriesAndCountV1,
            request_deserializer=lambda x: player_inventory_pb2.PlayerInventoryGetInventoriesAndCountV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_inventory_pb2.PlayerInventoryGetInventoriesAndCountV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.PlayerInventory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

