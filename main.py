from multiprocessing import freeze_support, Process
from time import sleep

import dns
import grpc_server
import lcx_server

_lcx_port = 9443
_dns_port = 53


if __name__ == "__main__":
    freeze_support()

    grpc_process = Process(target=grpc_server.serve, daemon=True)
    grpc_process.start()

    lcx_process = Process(
        target=lcx_server.start, args=(_lcx_port,), daemon=True)
    lcx_process.start()

    dns.start(_dns_port)

    try:
        grpc_process.join()
        lcx_server.join()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass

