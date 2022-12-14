from os import path
from ssl import PROTOCOL_TLS_SERVER, SSLContext
import sys
from wsgiref.simple_server import make_server

from assets import asset

# Port used by the asset server
_port = 443


def key_path():
    base_path = getattr(sys, '_MEIPASS', path.abspath('.'))
    return path.join(base_path, 'keys')


def application(environ, start_response):
    path = environ['PATH_INFO']
    if '/assets/' in path:
        path = path.split('/assets/')[1].split('?')[0]
    extension = path.split('.')[-1]
    content_type = 'application/octet-stream'
    if extension == 'txt':
        content_type = 'text/plain'
    elif extension == 'html':
        content_type = 'text/html'
    elif extension == 'css':
        content_type = 'text/css'
    elif extension == 'js':
        content_type = 'text/javascript'
    elif extension == 'jpg':
        content_type = 'image/jpeg'
    data = asset(path)

    status = '200 OK'
    headers = [
        ('Content-Type', content_type),
        # ('X-GUploader-UploadID', 'ADPycds88CrV2itY0zEFcG3w3j6PDaQDW8K4TfAWkwEWt2W0S-q0qXXXHI5aTbY7QEY27JkBe3XJv4eRsvfAh8ETotXFKDGANUg5'),
        # ('Last-Modified', 'Thu, 01 Jul 2021 13:03:54 GMT'),
        # ('ETag', '"6654c734ccab8f440ff0825eb443dc7f"'),
        # ('x-goog-generation', '1625144634611951'),
        # ('x-goog-metageneration', '1'),
        # ('x-goog-stored-content-encoding', 'identity'),
        # ('x-goog-stored-content-length', '2'),
        # ('Content-Type', 'text/plain'),
        # ('x-goog-hash', 'crc32c=5X841Q=='),
        # ('x-goog-hash', 'md5=ZlTHNMyrj0QP8IJetEPcfw=='),
        # ('x-goog-storage-class', 'REGIONAL'),
        # ('Accept-Ranges', 'bytes'),
        ('Content-Length', str(len(data))),
        # ('Server', 'UploadServer'),
        # ('Cache-Control', 'public, max-age=3600'),
        # ('Expires', 'Mon, 12 Dec 2022 09:00:52 GMT'),
        # ('Date', 'Mon, 12 Dec 2022 08:00:52 GMT'),
    ]
    start_response(status, headers)
    return [data]


def start(port):
    with make_server('', port, application) as httpd:
        certfile = path.join(key_path(), 'fullchain1.pem')
        keyfile = path.join(key_path(), 'privkey1.pem')
        context = SSLContext(PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile, keyfile)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

        print(f'Serving HTTPS on port {port}...')
        httpd.serve_forever()


if __name__ == '__main__':
    start(_port)

