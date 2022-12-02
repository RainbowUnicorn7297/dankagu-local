import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import friend_pb2
from takasho.schema.fes.player_api import friend_pb2_grpc


class Friend(friend_pb2_grpc.FriendServicer):
    
    def GetMyFollowersV1(self, request, context):
        response = friend_pb2.FriendGetMyFollowersV1.Response()
        return response


def add_FriendServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'FollowV1': grpc.unary_unary_rpc_method_handler(
            servicer.FollowV1,
            request_deserializer=lambda x: friend_pb2.FriendFollowV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendFollowV1.Response.SerializeToString(x)),
        ),
        'UnfollowV1': grpc.unary_unary_rpc_method_handler(
            servicer.UnfollowV1,
            request_deserializer=lambda x: friend_pb2.FriendUnfollowV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendUnfollowV1.Response.SerializeToString(x)),
        ),
        'RemoveMyFollowerV1': grpc.unary_unary_rpc_method_handler(
            servicer.RemoveMyFollowerV1,
            request_deserializer=lambda x: friend_pb2.FriendRemoveMyFollowerV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendRemoveMyFollowerV1.Response.SerializeToString(x)),
        ),
        'SearchPlayerByPlayerShortIDV1': grpc.unary_unary_rpc_method_handler(
            servicer.SearchPlayerByPlayerShortIDV1,
            request_deserializer=lambda x: friend_pb2.FriendSearchPlayerByPlayerShortIDV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendSearchPlayerByPlayerShortIDV1.Response.SerializeToString(x)),
        ),
        'GetMyFollowersV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetMyFollowersV1,
            request_deserializer=lambda x: friend_pb2.FriendGetMyFollowersV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendGetMyFollowersV1.Response.SerializeToString(x)),
        ),
        'GetMyFollowingsV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetMyFollowingsV1,
            request_deserializer=lambda x: friend_pb2.FriendGetMyFollowingsV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendGetMyFollowingsV1.Response.SerializeToString(x)),
        ),
        'GetRecentlyLoggedInPlayersV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetRecentlyLoggedInPlayersV1,
            request_deserializer=lambda x: friend_pb2.FriendGetRecentlyLoggedInPlayersV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendGetRecentlyLoggedInPlayersV1.Response.SerializeToString(x)),
        ),
        'GetFollowStatusesV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetFollowStatusesV1,
            request_deserializer=lambda x: friend_pb2.FriendGetFollowStatusesV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(friend_pb2.FriendGetFollowStatusesV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.friend.Friend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

