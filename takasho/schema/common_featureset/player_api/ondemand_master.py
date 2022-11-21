import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import ondemand_master_pb2
from takasho.schema.common_featureset.player_api import ondemand_master_pb2_grpc


class OndemandMaster(ondemand_master_pb2_grpc.OndemandMasterServicer):

    def GetEntriesV1(self, request, context):
        response = ondemand_master_pb2.OndemandMasterGetEntriesV2.Response()
        if 'ODMGeneric_Boot' in request.keys:
            entry = response.entries.add()
            entry.key = 'ODMGeneric_Boot'
            entry.value = b'[{"CloseAt":"4102444800","Enable":2,"ID":1,"Key":"TosVer","OpenAt":"0","Value":"v1"},{"CloseAt":"4102444800","Enable":2,"ID":2,"Key":"PPVer","OpenAt":"0","Value":"1"},{"CloseAt":"4102444800","Enable":2,"ID":3,"Key":"TosBaseUrl","OpenAt":"0","Value":"{AssetBase}/static/tos"},{"CloseAt":"4102444800","Enable":2,"ID":4,"Key":"PPBaseUrl","OpenAt":"0","Value":"{AssetBase}/static/pp"},{"CloseAt":"4102444800","Enable":2,"ID":5,"Key":"AccountLinkApealTime","OpenAt":"0","Value":"25920"},{"CloseAt":"4102444800","Enable":2,"ID":1001,"Key":"AdmobTester","OpenAt":"0","Value":""},{"CloseAt":"4102444800","Enable":2,"ID":1002,"Key":"AdmobTestDevice","OpenAt":"0","Value":""},{"CloseAt":"4102444800","Enable":2,"ID":1003,"Key":"AdmobAlwaysTestDevice","OpenAt":"0","Value":"0"},{"CloseAt":"4102444800","Enable":2,"ID":1004,"Key":"AdmobTestClientVersion","OpenAt":"0","Value":"1.5.0"},{"CloseAt":"4102444800","Enable":2,"ID":1011,"Key":"TestAdUnitId_A","OpenAt":"0","Value":"ca-app-pub-3940256099942544/5224354917"},{"CloseAt":"4102444800","Enable":2,"ID":1012,"Key":"TestAdUnitId_I","OpenAt":"0","Value":"ca-app-pub-3940256099942544/1712485313"},{"CloseAt":"4102444800","Enable":2,"ID":1013,"Key":"ProdAdUnitId_A","OpenAt":"0","Value":"ca-app-pub-9832876006157354/6112993928"},{"CloseAt":"4102444800","Enable":2,"ID":1014,"Key":"ProdAdUnitId_I","OpenAt":"0","Value":"ca-app-pub-9832876006157354/4664180889"},{"CloseAt":"4102444800","Enable":2,"ID":1015,"Key":"UseProdAdUnit","OpenAt":"0","Value":"1"},{"CloseAt":"4102444800","Enable":2,"ID":1016,"Key":"UseProdAdUnitOnDebugBuild","OpenAt":"0","Value":"0"}]'
        if 'ODMGeneric_SecureHash' in request.keys:
            entry = response.entries.add()
            entry.key = 'ODMGeneric_SecureHash'
            entry.value = b'[{"CloseAt":"4102444800","Enable":2,"ID":1,"Key":"MasterEnable","OpenAt":"0","Value":"1"},{"CloseAt":"4102444800","Enable":2,"ID":201001,"Key":"android_2.1.0_20220907","OpenAt":"0","Value":"9f982e6477b90db8,9a058678009df3c6,56f7d468f4f0b6a7,9b4992ecec388bb6,2b279e3205dc9193,15ce768b260f9767,0cbb624defb5dbd8,b21c75b736b8d7a0,666573c8725ab7f4,c1ea77db39d3f096,39a82b1e95ea910f,6d016f4c9dd0a17e,0f53ca016992d65d,85007dea29a1ef88,26b87af6aa7467b0,3d8b894d14b1e4b3,c09b0e7566b06014"},{"CloseAt":"4102444800","Enable":2,"ID":201002,"Key":"ios_2.1.0_20220907","OpenAt":"0","Value":"d538802bf56581e8"}]'
        if 'ODMGeneric_Signature' in request.keys:
            entry = response.entries.add()
            entry.key = 'ODMGeneric_Signature'
            entry.value = b'[{"CloseAt":"4102444800","Enable":2,"ID":1,"Key":"MasterEnable","OpenAt":"0","Value":"1"},{"CloseAt":"4102444800","Enable":2,"ID":2,"Key":"Sign_D","OpenAt":"0","Value":"db2d823ea4f7bcd40b6998a3b7a8adfd"},{"CloseAt":"4102444800","Enable":2,"ID":4,"Key":"Sign_X","OpenAt":"0","Value":"14b869b2ba7332f4d633f21932b57147"},{"CloseAt":"4102444800","Enable":2,"ID":5,"Key":"Sign_Xup","OpenAt":"0","Value":"cfb5a6c2695070d6642eb34b60e42048"}]'
        return response


def add_OndemandMasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEntriesV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntriesV1,
                    request_deserializer=lambda x: ondemand_master_pb2.OndemandMasterGetEntriesV2.Request.FromString(packer.unpack(x)),
                    response_serializer=lambda x: packer.pack(ondemand_master_pb2.OndemandMasterGetEntriesV2.Response.SerializeToString(x)),
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.common_featureset.player_api.OndemandMaster', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

