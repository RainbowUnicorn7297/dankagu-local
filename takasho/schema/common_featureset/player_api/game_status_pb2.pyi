from takasho.schema.common_featureset.resource.game_status import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameStatusGetV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["values"]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.Value]
        def __init__(self, values: _Optional[_Iterable[_Union[_v1_pb2.Value, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["statuses"]
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        statuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.Status]
        def __init__(self, statuses: _Optional[_Iterable[_Union[_v1_pb2.Status, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
