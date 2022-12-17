from inspect import cleandoc
from time import sleep

from dnslib.intercept import InterceptResolver
from dnslib.server import DNSServer
import netifaces

# Port used by the DNS server
_port = 53


def get_lan_ips():
    try:
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        ipv4 = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    except Exception:
        ipv4 = None
    try:
        iface = netifaces.gateways()['default'][netifaces.AF_INET6][1]
        ipv6 = netifaces.ifaddresses(iface)[netifaces.AF_INET6][0]['addr']
    except Exception:
        ipv6 = None
    return ipv4, ipv6


def start(port):
    lan_ipv4, lan_ipv6 = get_lan_ips()
    zone_record = ''
    if lan_ipv4:
        zone_record += cleandoc(f'''
            danmakujp4-local.lcx.tokyo. 60 IN A {lan_ipv4}
            danmakujp4-v1.lcx.tokyo. 60 IN A {lan_ipv4}
            player-api-local.dena-takasho.com. 60 IN A {lan_ipv4}
        ''')
        zone_record += '\n'
    if lan_ipv6:
        zone_record += cleandoc(f'''
            danmakujp4-local.lcx.tokyo. 60 IN AAAA {lan_ipv6}
            danmakujp4-v1.lcx.tokyo. 60 IN AAAA {lan_ipv6}
            player-api-local.dena-takasho.com. 60 IN AAAA {lan_ipv6}
        ''')
        zone_record += '\n'
    
    # Uncomment these lines to use local asset server
    # if lan_ipv4:
    #     zone_record += 'dankagu-assets.rainbowunicorn7297.com. 60 IN A ' \
    #         + '{lan_ipv4}\n'
    # if lan_ipv6:
    #     zone_record += 'dankagu-assets.rainbowunicorn7297.com. 60 IN AAAA ' \
    #         + '{lan_ipv6}\n'

    resolver = InterceptResolver(
        '8.8.8.8',     #upstream address
        53,            #upstream port
        '60s',         #ttl
        [zone_record], #incercept
        [],            #skip
        [],            #nxdomain
        [],            #forward
        False,         #all_qtypes
        5              #timeout
    )
    udp_server = DNSServer(resolver, port=port)
    print(f'DNS is running on port {port}...')
    udp_server.start_thread()


if __name__ == '__main__':
    start(_port)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass

