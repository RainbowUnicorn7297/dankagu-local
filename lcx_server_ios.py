from os import path
from ssl import PROTOCOL_TLS_SERVER, SSLContext
import sys
from wsgiref.simple_server import make_server

from handler import application

# Port used by the LCX server
_port = 443


def key_path():
    base_path = getattr(sys, '_MEIPASS', path.abspath('.'))
    return path.join(base_path, 'keys')


def start(port):
    with make_server('', port, application) as httpd:
        certfile = path.join(key_path(), 'lcx_ios.crt')
        keyfile = path.join(key_path(), 'lcx_ios.key')
        context = SSLContext(PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile, keyfile)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        # uncomment to debug SSL errors
##        httpd.socket.accept()

        print(f'Serving HTTPS on port {port}...')
        httpd.serve_forever()


if __name__ == "__main__":
    start(_port)

