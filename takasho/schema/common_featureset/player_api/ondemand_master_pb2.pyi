from takasho.schema.common_featureset.resource.ondemand_master import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OndemandMasterGetEntriesV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["keys"]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        def __init__(self, entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
