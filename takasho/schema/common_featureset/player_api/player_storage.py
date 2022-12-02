from pathlib import Path
import time

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import player_storage_pb2
from takasho.schema.common_featureset.player_api import player_storage_pb2_grpc


class PlayerStorage(player_storage_pb2_grpc.PlayerStorageServicer):
    
    def SetEntriesV2(self, request, context):
        response = player_storage_pb2.PlayerStorageSetEntriesV2.Response()
        response.entries.extend(request.entries)
        for entry in response.entries:
            entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
            entry.created_at = int(time.time())
            entry.updated_at = int(time.time())
        response.revision = request.next_revision
        return response
    
    def GetEntriesV2(self, request, context):
        response = player_storage_pb2.PlayerStorageGetEntriesV2.Response()
        entries_list = []
        for i in range(8):
            p = Path(__file__).with_name('player_storage.' + str(i) +'.hex')
            with p.open() as f:
                entries_list.append(
                    player_storage_pb2.PlayerStorageGetEntriesV2.Response. \
                        FromString(bytes.fromhex(f.read())).entries
                )
        for criterion in request.criteria:
            if criterion.key == 'PlayerBootStatus--':
                entry = response.entries.add()
                entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
                entry.key = 'PlayerBootStatus--1'
                entry.value = b'\010\001 \016(\001'
                entry.created_at = 1635215027
                entry.updated_at = 1663655102
            elif criterion.key == 'GpxInfoStatus-V1-':
                entry = response.entries.add()
                entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
                entry.key = 'GpxInfoStatus-V1-1'
                entry.value = b'\010\001\022*\010\250\214=\022\003\001\001\001\032\014\333\324\212\002\273\212\370\001\241\250\266\002"\014\333\324\212\002\320\376\361\001\241\250\266\002(\314\373\262\006\022*\010\220\224=\022\003\001\001\001\032\014\373\303\342\001\371\257\307\001\376\203\245\002"\014\373\303\342\001\371\257\307\001\376\203\245\002(\362\367\316\005\022$\010\370\233=\022\003\001\001\001\032\014\356\314\223\002\347\216\232\002\332\230\326\002"\006\000\000\240\320\303\002(\265\377\347\006\022*\010\340\243=\022\003\001\001\001\032\014\307\265\365\001\364\272\354\002\374\337\343\001"\014\262\374\362\001\364\272\354\002\374\337\343\001(\242\227\303\006\022\'\010\310\253=\022\003\001\001\001\032\014\212\376\240\002\261\276\307\002\210\227\315\002"\t\212\376\240\002\200\367\303\002\000(\273\357\252\007(\0050\0018\004@\310\253=H\264\272\223\232\006P\001X\001b$fa6306e0-3343-4016-bf2a-d24b6aa077bdh\357R'
                entry.created_at = 1659348369
                entry.updated_at = 1665458371
            elif criterion.key == 'CoopEventInfoStatus-V3-':
                entry = response.entries.add()
                entry.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
                entry.key = 'CoopEventInfoStatus-V3-3'
                entry.value = b'\010\003\022\004ddd\000\030\205\016 \220\302\233\232\006(\233\360\225\232\0060\216\231\001'
                entry.created_at = 1664525574
                entry.updated_at = 1665589520
            else:
                for entries in entries_list:
                    for e in entries:
                        if e.key.startswith(criterion.key):
                            response.entries.append(e)
            # 1st set
            # if criterion.key == 'AdMobMovieStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'CardEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'CardStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'CharacterEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'CharacterStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'ConstructionStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'DailyBonusStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'EpisodeEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'EpisodeStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'EventEmblemRankingStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'EventRaidAttackStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayerExpeditionChallengeStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'ExpeditionManageStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'ExpeditionMissionRecordEntityCollecttion--':
            #     entry = response.entries.add()
            # if criterion.key == 'Formation--':
            #     entry = response.entries.add()
            # if criterion.key == 'GachaTicketExchangeStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'GpxEntryStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'GrowthItemEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'GrowthItemStock--':
            #     entry = response.entries.add()
            # if criterion.key == 'HakoniwaStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'HeroineEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'HeroineStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'ImageHelpStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'ItemStockStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'MissionBeginnerStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'MissionControlStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'MissionCounterStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'MonthlyPassStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'MySpotItemStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'NakayosiCloudPairStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'NakayosiCloudPairtEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'PartyExecStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PKVSStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayCounterStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayerBase--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayerPublicStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayerSetting--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayerStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlayMusicRecord--':
            #     entry = response.entries.add()
            # if criterion.key == 'PlaySkipStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PremiumCardStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'ReconstructionStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'SaveHash--':
            #     entry = response.entries.add()
            # if criterion.key == 'ShopNewStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'ShopPurchaseStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'SpotObjectStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'SpotRepairObjectStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'SpotRepairStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'SpotRepairTutorialStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'SpotStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'SpotVisitStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'TutorialAdvStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'TweetStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'UnlockEntityStatusCollection--':
            #     entry = response.entries.add()
            # if criterion.key == 'UnlockStatus--':
            #     entry = response.entries.add()
            # 2nd set
            # if criterion.key == 'MissionStatusCollection-V1-':
            #     entry = response.entries.add()
            # 3rd set
            # if criterion.key == 'MissionStatusCollection-V10018-':
            #     entry = response.entries.add()
            # 4th set
            # if criterion.key == 'MissionStatusCollection-V10019-':
            #     entry = response.entries.add()
            # 5th set
            # if criterion.key == 'DanmakuPassSeasonStatus-V10014-':
            #     entry = response.entries.add()
            # 6th set
            # if criterion.key == 'DanmakuPassSeasonStatus-V10015-':
            #     entry = response.entries.add()
            # 7th set
            # if criterion.key == 'MySpotStatus--':
            #     entry = response.entries.add()
            # if criterion.key == 'PhotoStatus--':
            #     entry = response.entries.add()
            # 8th set
            # if criterion.key == 'JoinClubStatus--':
            #     entry = response.entries.add()
        response.revision = 'b69e1df8-2e05-48c9-bdb2-5a09bc8c7f4c'
        return response


def add_PlayerStorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SetEntriesV2': grpc.unary_unary_rpc_method_handler(
            servicer.SetEntriesV2,
            request_deserializer=lambda x: player_storage_pb2.PlayerStorageSetEntriesV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_storage_pb2.PlayerStorageSetEntriesV2.Response.SerializeToString(x)),
        ),
        'GetEntriesV2': grpc.unary_unary_rpc_method_handler(
            servicer.GetEntriesV2,
            request_deserializer=lambda x: player_storage_pb2.PlayerStorageGetEntriesV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_storage_pb2.PlayerStorageGetEntriesV2.Response.SerializeToString(x)),
        ),
        'GetOtherPlayerEntriesV2': grpc.unary_unary_rpc_method_handler(
            servicer.GetOtherPlayerEntriesV2,
            request_deserializer=lambda x: player_storage_pb2.PlayerStorageGetOtherPlayerEntriesV2.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(player_storage_pb2.PlayerStorageGetOtherPlayerEntriesV2.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.common_featureset.player_api.PlayerStorage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

