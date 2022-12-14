openssl req -x509 -newkey rsa:2048 -sha256 -nodes -keyout grpc.key -out grpc.crt -subj "/CN=player-api-local.dena-takasho.com" -days 36500
openssl req -x509 -newkey rsa:2048 -sha256 -nodes -keyout lcx.key -out lcx.crt -subj "/CN=danmakujp4-local.lcx.tokyo" -days 36500
