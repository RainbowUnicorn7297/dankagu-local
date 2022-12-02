import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api.subscription import renewal_reward_pb2
from takasho.schema.fes.player_api.subscription import renewal_reward_pb2_grpc


class RenewalReward(renewal_reward_pb2_grpc.RenewalRewardServicer):
    
    def ReceiveV1(self, request, context):
        response = renewal_reward_pb2.RenewalRewardReceiveV1.Response()
        renewal_count = response.renewal_counts.add()
        renewal_count.subscription_product_id = 'subs.currency.com.dena.game.12026801.mitamaishipass370'
        renewal_count.count = 12
        return response


def add_RenewalRewardServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: renewal_reward_pb2.RenewalRewardGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(renewal_reward_pb2.RenewalRewardGetAvailableV1.Response.SerializeToString(x)),
        ),
        'ReceiveV1': grpc.unary_unary_rpc_method_handler(
            servicer.ReceiveV1,
            request_deserializer=lambda x: renewal_reward_pb2.RenewalRewardReceiveV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(renewal_reward_pb2.RenewalRewardReceiveV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.subscription.renewal_reward.RenewalReward', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

