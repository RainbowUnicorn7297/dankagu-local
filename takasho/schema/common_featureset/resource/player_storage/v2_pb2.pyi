from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Criterion(_message.Message):
    __slots__ = ["key", "matching_type"]
    class MatchingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EXACT: Criterion.MatchingType
    FORWARD: Criterion.MatchingType
    KEY_FIELD_NUMBER: _ClassVar[int]
    MATCHING_TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    matching_type: Criterion.MatchingType
    def __init__(self, key: _Optional[str] = ..., matching_type: _Optional[_Union[Criterion.MatchingType, str]] = ...) -> None: ...

class Entry(_message.Message):
    __slots__ = ["created_at", "key", "player_id", "updated_at", "value"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    key: str
    player_id: str
    updated_at: int
    value: bytes
    def __init__(self, player_id: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[bytes] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...
