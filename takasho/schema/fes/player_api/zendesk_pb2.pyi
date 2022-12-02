from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ZendeskGetUnreadCountV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["unread_count"]
        UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
        unread_count: int
        def __init__(self, unread_count: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
