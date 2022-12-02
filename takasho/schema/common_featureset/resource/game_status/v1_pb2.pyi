from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Status(_message.Message):
    __slots__ = ["status", "value"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    value: int
    def __init__(self, value: _Optional[int] = ..., status: bool = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...
