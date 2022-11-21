from concurrent import futures
import logging

import grpc

from takasho.schema.common_featureset.player_api import ondemand_master, system


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    ondemand_master.add_OndemandMasterServicer_to_server(
        ondemand_master.OndemandMaster(), server)
    system.add_SystemServicer_to_server(system.System(), server)
    
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

