from pathlib import Path

import grpc

from takasho.packer import packer
from takasho.schema.common_featureset.player_api import announcement_pb2
from takasho.schema.common_featureset.player_api import announcement_pb2_grpc


class Announcement(announcement_pb2_grpc.AnnouncementServicer):
    
    def GetAvailableV1(self, request, context):
        p = Path(__file__).with_name(
            'announcement.' + str(request.max_results) + '.hex')
        with p.open() as f:
            response = announcement_pb2.AnnouncementGetAvailableV1.Response. \
                FromString(bytes.fromhex(f.read()))
        response.base_image_url = 'https://dankagu-assets.rainbowunicorn7297.com/assets/announcements'
        return response


def add_AnnouncementServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAvailableV1': grpc.unary_unary_rpc_method_handler(
            servicer.GetAvailableV1,
            request_deserializer=lambda x: announcement_pb2.AnnouncementGetAvailableV1.Request.FromString(packer.unpack(x)),
            response_serializer=lambda x: packer.pack(announcement_pb2.AnnouncementGetAvailableV1.Response.SerializeToString(x)),
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'takasho.schema.common_featureset.player_api.Announcement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

