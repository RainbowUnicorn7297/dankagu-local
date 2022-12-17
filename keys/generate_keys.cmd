openssl req -x509 -newkey rsa:2048 -sha256 -nodes -keyout grpc.key -out grpc.crt -subj "/CN=player-api-local.dena-takasho.com" -days 36500
openssl req -x509 -newkey rsa:2048 -sha256 -nodes -keyout lcx.key -out lcx.crt -subj "/CN=danmakujp4-local.lcx.tokyo" -days 36500
openssl req -x509 -newkey rsa:2048 -sha256 -nodes -keyout lcx_ios.key -out lcx_ios.crt -subj "/C=JP/ST=Tokyo/L=Shibuya-ku/O=DeNA Co., Ltd./CN=danmakujp4-v1.lcx.tokyo" -addext extendedKeyUsage=serverAuth -addext subjectAltName=DNS:danmakujp4-v1.lcx.tokyo -days 365
