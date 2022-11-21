python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/resource/ondemand_master/v2.proto
python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/player_api/ondemand_master.proto
python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/resource/system/v1.proto
python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/resource/player_event_log/v1.proto
python -m grpc_tools.protoc -I. --python_out=.. --pyi_out=.. --grpc_python_out=.. takasho/schema/common_featureset/player_api/system.proto
