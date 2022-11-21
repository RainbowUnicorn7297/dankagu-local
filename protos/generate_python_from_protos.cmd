python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/resource/ondemand_master/v2.proto
python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/player_api/ondemand_master.proto
