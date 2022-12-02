from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerStorageGetEntriesV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criteria"]
        CRITERIA_FIELD_NUMBER: _ClassVar[int]
        criteria: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Criterion]
        def __init__(self, criteria: _Optional[_Iterable[_Union[_v2_pb2.Criterion, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        revision: str
        def __init__(self, entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerStorageGetOtherPlayerEntriesV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criteria", "player_ids"]
        CRITERIA_FIELD_NUMBER: _ClassVar[int]
        PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
        criteria: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Criterion]
        player_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_ids: _Optional[_Iterable[str]] = ..., criteria: _Optional[_Iterable[_Union[_v2_pb2.Criterion, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        def __init__(self, entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerStorageSetEntriesV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "next_revision", "player_event_logs", "previous_revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerEventLog]
        previous_revision: str
        def __init__(self, entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        revision: str
        def __init__(self, entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
