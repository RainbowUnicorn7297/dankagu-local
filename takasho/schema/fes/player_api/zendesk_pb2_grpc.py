# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.fes.player_api import zendesk_pb2 as takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2


class ZendeskStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUnreadCountV1 = channel.unary_unary(
                '/takasho.schema.fes.player_api.Zendesk/GetUnreadCountV1',
                request_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2.ZendeskGetUnreadCountV1.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2.ZendeskGetUnreadCountV1.Response.FromString,
                )


class ZendeskServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUnreadCountV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ZendeskServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUnreadCountV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUnreadCountV1,
                    request_deserializer=takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2.ZendeskGetUnreadCountV1.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2.ZendeskGetUnreadCountV1.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.fes.player_api.Zendesk', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Zendesk(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUnreadCountV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.fes.player_api.Zendesk/GetUnreadCountV1',
            takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2.ZendeskGetUnreadCountV1.Request.SerializeToString,
            takasho_dot_schema_dot_fes_dot_player__api_dot_zendesk__pb2.ZendeskGetUnreadCountV1.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
