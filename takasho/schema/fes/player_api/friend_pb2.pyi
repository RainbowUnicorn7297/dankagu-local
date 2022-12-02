from takasho.schema.fes.resource.friend import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendFollowV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "player_id"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_id: str
        def __init__(self, player_id: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class FriendGetFollowStatusesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_ids"]
        PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
        player_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["follow_statuses"]
        FOLLOW_STATUSES_FIELD_NUMBER: _ClassVar[int]
        follow_statuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.FollowStatus]
        def __init__(self, follow_statuses: _Optional[_Iterable[_Union[_v1_pb2.FollowStatus, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class FriendGetMyFollowersV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion", "max_results", "page_token", "player_storage_keys"]
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        criterion: _v1_pb2.Criterion
        max_results: int
        page_token: str
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_storage_keys: _Optional[_Iterable[str]] = ..., criterion: _Optional[_Union[_v1_pb2.Criterion, _Mapping]] = ..., page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["next_page_token", "players", "prev_page_token"]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        next_page_token: str
        players: _containers.RepeatedCompositeFieldContainer[_v1_pb2.FriendPlayer]
        prev_page_token: str
        def __init__(self, players: _Optional[_Iterable[_Union[_v1_pb2.FriendPlayer, _Mapping]]] = ..., prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class FriendGetMyFollowingsV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion", "max_results", "page_token", "player_storage_keys"]
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        criterion: _v1_pb2.Criterion
        max_results: int
        page_token: str
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_storage_keys: _Optional[_Iterable[str]] = ..., criterion: _Optional[_Union[_v1_pb2.Criterion, _Mapping]] = ..., page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["next_page_token", "players", "prev_page_token"]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        next_page_token: str
        players: _containers.RepeatedCompositeFieldContainer[_v1_pb2.FriendPlayer]
        prev_page_token: str
        def __init__(self, players: _Optional[_Iterable[_Union[_v1_pb2.FriendPlayer, _Mapping]]] = ..., prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class FriendGetRecentlyLoggedInPlayersV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion", "max_results", "page_token", "player_storage_keys"]
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        criterion: _v1_pb2.Criterion
        max_results: int
        page_token: str
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_storage_keys: _Optional[_Iterable[str]] = ..., criterion: _Optional[_Union[_v1_pb2.Criterion, _Mapping]] = ..., page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["next_page_token", "players", "prev_page_token"]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        next_page_token: str
        players: _containers.RepeatedCompositeFieldContainer[_v1_pb2.FriendPlayer]
        prev_page_token: str
        def __init__(self, players: _Optional[_Iterable[_Union[_v1_pb2.FriendPlayer, _Mapping]]] = ..., prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class FriendRemoveMyFollowerV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "player_id"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_id: str
        def __init__(self, player_id: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class FriendSearchPlayerByPlayerShortIDV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_short_id", "player_storage_keys"]
        PLAYER_SHORT_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        player_short_id: str
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_short_id: _Optional[str] = ..., player_storage_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player"]
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        player: _v1_pb2.FriendPlayer
        def __init__(self, player: _Optional[_Union[_v1_pb2.FriendPlayer, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class FriendUnfollowV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "player_id"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_id: str
        def __init__(self, player_id: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
