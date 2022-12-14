from takasho.schema.fes.resource.player_regular_ranking import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegularRankingGetTopRankingV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["count", "ranking_key", "start"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        RANKING_KEY_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        count: int
        ranking_key: str
        start: int
        def __init__(self, ranking_key: _Optional[str] = ..., start: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_rankings"]
        PLAYER_RANKINGS_FIELD_NUMBER: _ClassVar[int]
        player_rankings: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerRegularRanking]
        def __init__(self, player_rankings: _Optional[_Iterable[_Union[_v1_pb2.PlayerRegularRanking, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class RegularRankingRegisterV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["ranking_key", "score"]
        RANKING_KEY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        ranking_key: str
        score: int
        def __init__(self, ranking_key: _Optional[str] = ..., score: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_ranking"]
        PLAYER_RANKING_FIELD_NUMBER: _ClassVar[int]
        player_ranking: _v1_pb2.PlayerRegularRanking
        def __init__(self, player_ranking: _Optional[_Union[_v1_pb2.PlayerRegularRanking, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
