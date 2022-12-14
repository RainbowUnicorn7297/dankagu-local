from pathlib import Path

import grpc

from takasho.packer import packer
from takasho.schema.fes.player_api import login_bonus_pb2
from takasho.schema.fes.player_api import login_bonus_pb2_grpc


class LoginBonus(login_bonus_pb2_grpc.LoginBonusServicer):
    
    def GetAvailableLoginBonusV1(self, request, context):
        response = login_bonus_pb2.LoginBonusGetAvailableV1.Response()
        # p = Path(__file__).with_name('login_bonus.GetAvailableV1.hex')
        # with p.open() as f:
        #     response = login_bonus_pb2.LoginBonusGetAvailableV1.Response. \
        #         FromString(bytes.fromhex(f.read()))
        return response
    
    def CountUpProgressV1(self, request, context):
        response = login_bonus_pb2.LoginBonusCountUpProgressV1.Response()
        # p = Path(__file__).with_name('login_bouns.CountUpProgressV1.hex')
        # with p.open() as f:
        #     response = login_bonus_pb2.LoginBonusCountUpProgressV1.Response. \
        #         FromString(bytes.fromhex(f.read()))
        return response


def add_LoginBonusServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CountUpProgressV1': grpc.unary_unary_rpc_method_handler(
            servicer.CountUpProgressV1,
            request_deserializer=lambda x: login_bonus_pb2.LoginBonusCountUpProgressV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(login_bonus_pb2.LoginBonusCountUpProgressV1.Response.SerializeToString(x)),
        ),
        'GetAvailableLoginBonusV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableLoginBonusV1,
            request_deserializer=lambda x: login_bonus_pb2.LoginBonusGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(login_bonus_pb2.LoginBonusGetAvailableV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.fes.player_api.LoginBonus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

