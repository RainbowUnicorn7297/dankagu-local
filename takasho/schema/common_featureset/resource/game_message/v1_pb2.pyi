from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GameMessage(_message.Message):
    __slots__ = ["created_at", "extra", "is_received", "message", "message_id", "title"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    IS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    extra: bytes
    is_received: bool
    message: str
    message_id: str
    title: str
    def __init__(self, message_id: _Optional[str] = ..., is_received: bool = ..., title: _Optional[str] = ..., message: _Optional[str] = ..., extra: _Optional[bytes] = ..., created_at: _Optional[int] = ...) -> None: ...
