import time

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import system_pb2
from takasho.schema.common_featureset.player_api import system_pb2_grpc


class System(system_pb2_grpc.SystemServicer):

    def AuthorizeV3(self, request, context):
        response = system_pb2.SystemAuthorizeV3.Response()
        response.session_token = 'sbyOO27RqOw47sqekjgogR279Vyfl/NTFYiNgtKvSvw5vp5IcL0hmqPNvnE/Hxp2IoAAFP5/+v8VFX+JGHX9tJYnvh/vdvUiWy1StAg9wnjyarn6G62hqI9FIqe1yHL4U5xPVbUXDx0+EZ2I+m1/kuYtVKgc+F5lQipP/HzULtREZfIEpUNFi63gMjmB0Ikg'
        response.player_id = 'b7124b56-3fa4-427a-8dd0-64ec8830294e'
        return response
    
    def RecordLoginHistoryV1(self, request, context):
        response = system_pb2.SystemRecordLoginHistoryV1.Response()
        response.logged_in_at = int(time.time())
        return response


def add_SystemServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'AuthorizeV3': grpc.unary_unary_rpc_method_handler(
                servicer.AuthorizeV3,
                request_deserializer=lambda x: system_pb2.SystemAuthorizeV3.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemAuthorizeV3.Response.SerializeToString(x)),
        ),
        'AuthorizeV2': grpc.unary_unary_rpc_method_handler(
                servicer.AuthorizeV2,
                request_deserializer=lambda x: system_pb2.SystemAuthorizeV2.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemAuthorizeV2.Response.SerializeToString(x)),
        ),
        'GetPlayerStatusV1': grpc.unary_unary_rpc_method_handler(
                servicer.GetPlayerStatusV1,
                request_deserializer=lambda x: system_pb2.SystemGetPlayerStatusV1.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemGetPlayerStatusV1.Response.SerializeToString(x)),
        ),
        'GetPlayerStatusV2': grpc.unary_unary_rpc_method_handler(
                servicer.GetPlayerStatusV2,
                request_deserializer=lambda x: system_pb2.SystemGetPlayerStatusV2.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemGetPlayerStatusV2.Response.SerializeToString(x)),
        ),
        'SetPlayerStatusV1': grpc.unary_unary_rpc_method_handler(
                servicer.SetPlayerStatusV1,
                request_deserializer=lambda x: system_pb2.SystemSetPlayerStatusV1.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemSetPlayerStatusV1.Response.SerializeToString(x)),
        ),
        'DeletePlayerStatusV1': grpc.unary_unary_rpc_method_handler(
                servicer.DeletePlayerStatusV1,
                request_deserializer=lambda x: system_pb2.SystemDeletePlayerStatusV1.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemDeletePlayerStatusV1.Response.SerializeToString(x)),
        ),
        'RecordLoginHistoryV1': grpc.unary_unary_rpc_method_handler(
                servicer.RecordLoginHistoryV1,
                request_deserializer=lambda x: system_pb2.SystemRecordLoginHistoryV1.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemRecordLoginHistoryV1.Response.SerializeToString(x)),
        ),
        'GetWebTokenV1': grpc.unary_unary_rpc_method_handler(
                servicer.GetWebTokenV1,
                request_deserializer=lambda x: system_pb2.SystemGetWebTokenV1.Request.FromString(packer.unpack(x)),
                response_serializer=lambda x: packer.pack(system_pb2.SystemGetWebTokenV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.System', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

