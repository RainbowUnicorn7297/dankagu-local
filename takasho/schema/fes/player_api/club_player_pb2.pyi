from takasho.schema.fes.resource.club_storage import v1_pb2 as _v1_pb2
from takasho.schema.fes.resource.club import v1_pb2 as _v1_pb2_1
from takasho.schema.fes.resource.club_player import v1_pb2 as _v1_pb2_1_1
from takasho.schema.fes.resource.club_role import v1_pb2 as _v1_pb2_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClubPlayerGetClubs(_message.Message):
    __slots__ = []
    class ClubWithFrame(_message.Message):
        __slots__ = ["club", "frame"]
        CLUB_FIELD_NUMBER: _ClassVar[int]
        FRAME_FIELD_NUMBER: _ClassVar[int]
        club: _v1_pb2_1.Club
        frame: int
        def __init__(self, club: _Optional[_Union[_v1_pb2_1.Club, _Mapping]] = ..., frame: _Optional[int] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ["criteria", "player_id"]
        CRITERIA_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        criteria: _containers.RepeatedCompositeFieldContainer[_v1_pb2.Criterion]
        player_id: str
        def __init__(self, player_id: _Optional[str] = ..., criteria: _Optional[_Iterable[_Union[_v1_pb2.Criterion, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["clubs"]
        CLUBS_FIELD_NUMBER: _ClassVar[int]
        clubs: _containers.RepeatedCompositeFieldContainer[ClubPlayerGetClubs.ClubWithFrame]
        def __init__(self, clubs: _Optional[_Iterable[_Union[ClubPlayerGetClubs.ClubWithFrame, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ClubPlayerGetPlayers(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["club_id", "player_storage_keys"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, club_id: _Optional[str] = ..., player_storage_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["club_players"]
        CLUB_PLAYERS_FIELD_NUMBER: _ClassVar[int]
        club_players: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.ClubPlayer]
        def __init__(self, club_players: _Optional[_Iterable[_Union[_v1_pb2_1_1.ClubPlayer, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ClubPlayerGetPlayersCount(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["club_id"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        def __init__(self, club_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["players_count"]
        PLAYERS_COUNT_FIELD_NUMBER: _ClassVar[int]
        players_count: int
        def __init__(self, players_count: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class ClubPlayerKickPlayer(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["club_id", "player_id"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        player_id: str
        def __init__(self, club_id: _Optional[str] = ..., player_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class ClubPlayerLeave(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["club_id"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        def __init__(self, club_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class ClubPlayerUpdateRole(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["club_id", "player_id", "type"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        player_id: str
        type: _v1_pb2_1_1_1.ClubUpdateRoleType
        def __init__(self, club_id: _Optional[str] = ..., player_id: _Optional[str] = ..., type: _Optional[_Union[_v1_pb2_1_1_1.ClubUpdateRoleType, str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
