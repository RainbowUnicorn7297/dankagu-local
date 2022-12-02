from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from takasho.schema.fes.resource.club_role import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClubPlayer(_message.Message):
    __slots__ = ["frame", "joined_at", "last_logged_in_at", "nickname", "player_id", "player_short_id", "player_storage_entries", "role"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGGED_IN_AT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SHORT_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STORAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    frame: int
    joined_at: int
    last_logged_in_at: int
    nickname: str
    player_id: str
    player_short_id: str
    player_storage_entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
    role: _v1_pb2.ClubRole
    def __init__(self, player_id: _Optional[str] = ..., player_storage_entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., nickname: _Optional[str] = ..., frame: _Optional[int] = ..., role: _Optional[_Union[_v1_pb2.ClubRole, str]] = ..., joined_at: _Optional[int] = ..., last_logged_in_at: _Optional[int] = ..., player_short_id: _Optional[str] = ...) -> None: ...
