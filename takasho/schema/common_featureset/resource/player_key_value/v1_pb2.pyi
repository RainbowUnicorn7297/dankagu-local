from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DECREASE: OperationType
DESCRIPTOR: _descriptor.FileDescriptor
INCREASE: OperationType
UNKNOWN: OperationType

class PlayerKeyValue(_message.Message):
    __slots__ = ["expired_at", "key", "value"]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    expired_at: int
    key: str
    value: int
    def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ..., expired_at: _Optional[int] = ...) -> None: ...

class PlayerKeyValueIncrementInfo(_message.Message):
    __slots__ = ["delta", "key"]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    delta: int
    key: str
    def __init__(self, key: _Optional[str] = ..., delta: _Optional[int] = ...) -> None: ...

class PlayerKeyValueUpdateInfo(_message.Message):
    __slots__ = ["amount", "key"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    amount: int
    key: str
    def __init__(self, key: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
