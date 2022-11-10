from wsgiref.simple_server import make_server

from assets import asset

# Port used by the asset server
_port = 8080

def application(environ, start_response):
    path = environ['PATH_INFO'].split('/data/')[1]
    data = asset(path)

    status = '200 OK'
    headers = [
        ('Content-Type', 'application/octet-stream'),
        ('Content-Length', len(data))
    ]
    start_response(status, headers)
    return data

def start(port):
    with make_server('', port, application) as httpd:
        print(f'Serving HTTP on port {port}...')
        httpd.serve_forever()

if __name__ == "__main__":
    start(_port)
