from takasho.schema.fes.resource.reconstruction_spot import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReconstructionSpotGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["spots"]
        SPOTS_FIELD_NUMBER: _ClassVar[int]
        spots: _containers.RepeatedCompositeFieldContainer[_v1_pb2.Spot]
        def __init__(self, spots: _Optional[_Iterable[_Union[_v1_pb2.Spot, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ReconstructionSpotReceivePrizesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        def __init__(self, player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["inventories"]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        def __init__(self, inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
