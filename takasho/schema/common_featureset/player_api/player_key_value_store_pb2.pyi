from takasho.schema.common_featureset.resource.player_key_value import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerKeyValueStoreGetPlayerKeyValuesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["key"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_key_values"]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValue]
        def __init__(self, player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValue, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerKeyValueStoreIncrementPlayerKeyValuesAndSavePlayerStorageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "next_revision", "player_event_logs", "player_key_values", "previous_revision", "transaction_id"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValueIncrementInfo]
        previous_revision: str
        transaction_id: str
        def __init__(self, transaction_id: _Optional[str] = ..., player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValueIncrementInfo, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "player_key_values", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValue]
        revision: str
        def __init__(self, player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValue, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerKeyValueStoreIncrementPlayerKeyValuesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "player_key_values", "transaction_id"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValueIncrementInfo]
        transaction_id: str
        def __init__(self, transaction_id: _Optional[str] = ..., player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValueIncrementInfo, _Mapping]]] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_key_values"]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValue]
        def __init__(self, player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValue, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerKeyValueStoreUpdatePlayerKeyValuesAndSavePlayerStorageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "next_revision", "player_event_logs", "player_key_values", "previous_revision", "transaction_id"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValueUpdateInfo]
        previous_revision: str
        transaction_id: str
        def __init__(self, transaction_id: _Optional[str] = ..., player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValueUpdateInfo, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "player_key_values", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerKeyValue]
        revision: str
        def __init__(self, player_key_values: _Optional[_Iterable[_Union[_v1_pb2.PlayerKeyValue, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
