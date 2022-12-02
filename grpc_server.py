from concurrent import futures
import logging

import grpc

from takasho.schema.common_featureset.player_api import baas_product, \
    game_product, game_status, loot_box, player_inventory, player_preference, \
    player_storage, push_notification, ondemand_master, step_up_loot_box, \
    system, wallet
from takasho.schema.fes.player_api import club_player, friend, \
    reconstruction_spot, score_ranking, zendesk
from takasho.schema.fes.player_api import player_preference \
    as fes_player_preference
from takasho.schema.fes.player_api.subscription import renewal_reward


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    ondemand_master.add_OndemandMasterServicer_to_server(
        ondemand_master.OndemandMaster(), server)
    system.add_SystemServicer_to_server(system.System(), server)
    zendesk.add_ZendeskServicer_to_server(zendesk.Zendesk(), server)
    player_preference.add_PlayerPreferenceServicer_to_server(
        player_preference.PlayerPreference(), server)
    player_storage.add_PlayerStorageServicer_to_server(
        player_storage.PlayerStorage(), server)
    fes_player_preference.add_FesPlayerPreferenceServicer_to_server(
        fes_player_preference.FesPlayerPreference(), server)
    push_notification.add_PushNotificationServicer_to_server(
        push_notification.PushNotification(), server)
    game_status.add_GameStatusServicer_to_server(
        game_status.GameStatus(), server)
    game_product.add_GameProductServicer_to_server(
        game_product.GameProduct(), server)
    wallet.add_WalletServicer_to_server(wallet.Wallet(), server)
    player_inventory.add_PlayerInventoryServicer_to_server(
        player_inventory.PlayerInventory(), server)
    friend.add_FriendServicer_to_server(friend.Friend(), server)
    score_ranking.add_ScoreRankingServicer_to_server(
        score_ranking.ScoreRanking(), server)
    loot_box.add_LootBoxServicer_to_server(loot_box.LootBox(), server)
    step_up_loot_box.add_StepUpLootBoxServicer_to_server(
        step_up_loot_box.StepUpLootBox(), server)
    club_player.add_ClubPlayerServicer_to_server(
        club_player.ClubPlayer(), server)
    baas_product.add_BaasProductServicer_to_server(
        baas_product.BaasProduct(), server)
    renewal_reward.add_RenewalRewardServicer_to_server(
        renewal_reward.RenewalReward(), server)
    reconstruction_spot.add_ReconstructionSpotServicer_to_server(
        reconstruction_spot.ReconstructionSpot(), server)
    
    with open('keys/grpc.key', 'rb') as f:
        private_key = f.read()
    with open('keys/grpc.crt', 'rb') as f:
        certificate_chain = f.read()
    credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)])
    server.add_secure_port('[::]:' + port, credentials)
    server.start()
    print('Server started, listening on ' + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

