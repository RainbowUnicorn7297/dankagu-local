from takasho.schema.fes.resource.player_preference import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FesPlayerPreferenceGetV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_preference"]
        PLAYER_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        player_preference: _v1_pb2.PlayerPreference
        def __init__(self, player_preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class FesPlayerPreferenceSetAndSavePlayerStorageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "next_revision", "player_event_logs", "player_preference", "previous_revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_preference: _v1_pb2.PlayerPreference
        previous_revision: str
        def __init__(self, player_preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "player_preference", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        player_preference: _v1_pb2.PlayerPreference
        revision: str
        def __init__(self, player_preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
