from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerRegularRanking(_message.Message):
    __slots__ = ["nick_name", "player_id", "rank", "ranking_key", "score"]
    NICK_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    RANKING_KEY_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    nick_name: str
    player_id: str
    rank: int
    ranking_key: str
    score: int
    def __init__(self, ranking_key: _Optional[str] = ..., player_id: _Optional[str] = ..., nick_name: _Optional[str] = ..., rank: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...
