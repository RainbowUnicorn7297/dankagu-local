from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACHIEVEMENT: MessageType
COMMENT: MessageType
DESCRIPTOR: _descriptor.FileDescriptor
NOTIFICATION: MessageType
STAMP: MessageType
UNKNOWN: MessageType

class ClubChatMessage(_message.Message):
    __slots__ = ["club_id", "content", "message_id", "message_type", "player", "posted_at"]
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    POSTED_AT_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    content: str
    message_id: str
    message_type: MessageType
    player: ClubChatMessagePlayer
    posted_at: int
    def __init__(self, club_id: _Optional[str] = ..., message_id: _Optional[str] = ..., message_type: _Optional[_Union[MessageType, str]] = ..., content: _Optional[str] = ..., player: _Optional[_Union[ClubChatMessagePlayer, _Mapping]] = ..., posted_at: _Optional[int] = ...) -> None: ...

class ClubChatMessagePlayer(_message.Message):
    __slots__ = ["nickname", "player_id", "player_storage_entries"]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STORAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    player_id: str
    player_storage_entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
    def __init__(self, player_id: _Optional[str] = ..., nickname: _Optional[str] = ..., player_storage_entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ...) -> None: ...

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
