# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from takasho.schema.common_featureset.player_api import ondemand_master_pb2 as takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2


class OndemandMasterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEntriesV1 = channel.unary_unary(
                '/takasho.schema.common_featureset.player_api.OndemandMaster/GetEntriesV1',
                request_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2.OndemandMasterGetEntriesV2.Request.SerializeToString,
                response_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2.OndemandMasterGetEntriesV2.Response.FromString,
                )


class OndemandMasterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEntriesV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OndemandMasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEntriesV1': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntriesV1,
                    request_deserializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2.OndemandMasterGetEntriesV2.Request.FromString,
                    response_serializer=takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2.OndemandMasterGetEntriesV2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'takasho.schema.common_featureset.player_api.OndemandMaster', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OndemandMaster(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEntriesV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/takasho.schema.common_featureset.player_api.OndemandMaster/GetEntriesV1',
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2.OndemandMasterGetEntriesV2.Request.SerializeToString,
            takasho_dot_schema_dot_common__featureset_dot_player__api_dot_ondemand__master__pb2.OndemandMasterGetEntriesV2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
