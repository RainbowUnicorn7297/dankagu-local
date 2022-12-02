from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerPreference(_message.Message):
    __slots__ = ["is_my_space_released", "player_id", "player_level"]
    IS_MY_SPACE_RELEASED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    is_my_space_released: bool
    player_id: str
    player_level: int
    def __init__(self, player_id: _Optional[str] = ..., player_level: _Optional[int] = ..., is_my_space_released: bool = ...) -> None: ...
