from takasho.schema.fes.resource.score_ranking import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScoreRankingEntryV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_class"]
        PLAYER_CLASS_FIELD_NUMBER: _ClassVar[int]
        player_class: _v1_pb2.PlayerClass
        def __init__(self, player_class: _Optional[_Union[_v1_pb2.PlayerClass, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["season"]
        SEASON_FIELD_NUMBER: _ClassVar[int]
        season: _v1_pb2.Season
        def __init__(self, season: _Optional[_Union[_v1_pb2.Season, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetClassGroupElevatingRankV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["class_id", "group_id", "period_id"]
        CLASS_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        PERIOD_ID_FIELD_NUMBER: _ClassVar[int]
        class_id: str
        group_id: str
        period_id: str
        def __init__(self, period_id: _Optional[str] = ..., class_id: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["demotion_rank", "promotion_rank"]
        DEMOTION_RANK_FIELD_NUMBER: _ClassVar[int]
        PROMOTION_RANK_FIELD_NUMBER: _ClassVar[int]
        demotion_rank: int
        promotion_rank: int
        def __init__(self, promotion_rank: _Optional[int] = ..., demotion_rank: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetClassGroupLeaderBoardV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["count", "player_storage_keys", "start"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        count: int
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        start: int
        def __init__(self, start: _Optional[int] = ..., count: _Optional[int] = ..., player_storage_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_rank_infos"]
        PLAYER_RANK_INFOS_FIELD_NUMBER: _ClassVar[int]
        player_rank_infos: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerClassGroupRankingInfo]
        def __init__(self, player_rank_infos: _Optional[_Iterable[_Union[_v1_pb2.PlayerClassGroupRankingInfo, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetClassGroupRankV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["period_id", "player_ids"]
        PERIOD_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
        period_id: str
        player_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_ids: _Optional[_Iterable[str]] = ..., period_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_class_group_rank_infos"]
        PLAYER_CLASS_GROUP_RANK_INFOS_FIELD_NUMBER: _ClassVar[int]
        player_class_group_rank_infos: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerClassGroupRankInfo]
        def __init__(self, player_class_group_rank_infos: _Optional[_Iterable[_Union[_v1_pb2.PlayerClassGroupRankInfo, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetClassV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["period_id", "player_ids"]
        PERIOD_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
        period_id: str
        player_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_ids: _Optional[_Iterable[str]] = ..., period_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_classes"]
        PLAYER_CLASSES_FIELD_NUMBER: _ClassVar[int]
        player_classes: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerClass]
        def __init__(self, player_classes: _Optional[_Iterable[_Union[_v1_pb2.PlayerClass, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetGrandPrixLeaderBoardV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["count", "player_storage_keys", "start"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        count: int
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        start: int
        def __init__(self, start: _Optional[int] = ..., count: _Optional[int] = ..., player_storage_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["is_during_aggregation", "player_rank_infos"]
        IS_DURING_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_RANK_INFOS_FIELD_NUMBER: _ClassVar[int]
        is_during_aggregation: bool
        player_rank_infos: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerGrandPrixRankingInfo]
        def __init__(self, player_rank_infos: _Optional[_Iterable[_Union[_v1_pb2.PlayerGrandPrixRankingInfo, _Mapping]]] = ..., is_during_aggregation: bool = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingGetGrandPrixRankV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_ids"]
        PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
        player_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, player_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["is_during_aggregation", "player_grand_prix_rank_infos"]
        IS_DURING_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_GRAND_PRIX_RANK_INFOS_FIELD_NUMBER: _ClassVar[int]
        is_during_aggregation: bool
        player_grand_prix_rank_infos: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerGrandPrixRankInfo]
        def __init__(self, player_grand_prix_rank_infos: _Optional[_Iterable[_Union[_v1_pb2.PlayerGrandPrixRankInfo, _Mapping]]] = ..., is_during_aggregation: bool = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingReceiveClassPrizeV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_period_class_prize_infos"]
        PLAYER_PERIOD_CLASS_PRIZE_INFOS_FIELD_NUMBER: _ClassVar[int]
        player_period_class_prize_infos: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerPeriodClassPrizeInfo]
        def __init__(self, player_period_class_prize_infos: _Optional[_Iterable[_Union[_v1_pb2.PlayerPeriodClassPrizeInfo, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingReceiveGrandPrixPrizeV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["inventories", "rank"]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerInventory]
        rank: int
        def __init__(self, rank: _Optional[int] = ..., inventories: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerInventory, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ScoreRankingRegisterV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["score"]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        score: int
        def __init__(self, score: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["rank", "score"]
        RANK_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        rank: int
        score: int
        def __init__(self, score: _Optional[int] = ..., rank: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
