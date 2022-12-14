from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Announcement(_message.Message):
    __slots__ = ["closed_at", "contents", "id", "language_code", "opened_at", "title", "value"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    contents: _containers.RepeatedCompositeFieldContainer[AnnouncementContent]
    id: str
    language_code: str
    opened_at: int
    title: str
    value: bytes
    def __init__(self, id: _Optional[str] = ..., language_code: _Optional[str] = ..., title: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., value: _Optional[bytes] = ..., contents: _Optional[_Iterable[_Union[AnnouncementContent, _Mapping]]] = ...) -> None: ...

class AnnouncementContent(_message.Message):
    __slots__ = ["schema_key", "value"]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    schema_key: str
    value: bytes
    def __init__(self, schema_key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
