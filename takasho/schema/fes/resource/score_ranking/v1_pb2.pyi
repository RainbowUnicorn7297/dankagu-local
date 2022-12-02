from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClassGroupPrize(_message.Message):
    __slots__ = ["class_ranking_grand_prix_points", "ranking_prizes"]
    CLASS_RANKING_GRAND_PRIX_POINTS_FIELD_NUMBER: _ClassVar[int]
    RANKING_PRIZES_FIELD_NUMBER: _ClassVar[int]
    class_ranking_grand_prix_points: _containers.RepeatedCompositeFieldContainer[ClassRankingGrandPrixPointPrize]
    ranking_prizes: _containers.RepeatedCompositeFieldContainer[RankingPrize]
    def __init__(self, ranking_prizes: _Optional[_Iterable[_Union[RankingPrize, _Mapping]]] = ..., class_ranking_grand_prix_points: _Optional[_Iterable[_Union[ClassRankingGrandPrixPointPrize, _Mapping]]] = ...) -> None: ...

class ClassPrize(_message.Message):
    __slots__ = ["class_id", "prizes"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    PRIZES_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    prizes: _containers.RepeatedCompositeFieldContainer[Prize]
    def __init__(self, class_id: _Optional[str] = ..., prizes: _Optional[_Iterable[_Union[Prize, _Mapping]]] = ...) -> None: ...

class ClassRankingGrandPrixPointPrize(_message.Message):
    __slots__ = ["end_rank", "point", "start_rank", "value"]
    END_RANK_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    START_RANK_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    end_rank: int
    point: int
    start_rank: int
    value: bytes
    def __init__(self, start_rank: _Optional[int] = ..., end_rank: _Optional[int] = ..., point: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class Period(_message.Message):
    __slots__ = ["class_group_prizes", "class_prizes", "closed_at", "finished_at", "opened_at", "period_id"]
    CLASS_GROUP_PRIZES_FIELD_NUMBER: _ClassVar[int]
    CLASS_PRIZES_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_ID_FIELD_NUMBER: _ClassVar[int]
    class_group_prizes: ClassGroupPrize
    class_prizes: _containers.RepeatedCompositeFieldContainer[ClassPrize]
    closed_at: int
    finished_at: int
    opened_at: int
    period_id: str
    def __init__(self, period_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., finished_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., class_prizes: _Optional[_Iterable[_Union[ClassPrize, _Mapping]]] = ..., class_group_prizes: _Optional[_Union[ClassGroupPrize, _Mapping]] = ...) -> None: ...

class PlayerClass(_message.Message):
    __slots__ = ["class_id", "group_id", "player_id", "score"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    group_id: str
    player_id: str
    score: int
    def __init__(self, player_id: _Optional[str] = ..., class_id: _Optional[str] = ..., score: _Optional[int] = ..., group_id: _Optional[str] = ...) -> None: ...

class PlayerClassGroupRankInfo(_message.Message):
    __slots__ = ["player_id", "rank", "score"]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    player_id: str
    rank: int
    score: int
    def __init__(self, player_id: _Optional[str] = ..., rank: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...

class PlayerClassGroupRankingInfo(_message.Message):
    __slots__ = ["class_id", "level", "nickname", "player_id", "player_storage_entries", "rank", "score"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STORAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    level: int
    nickname: str
    player_id: str
    player_storage_entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
    rank: int
    score: int
    def __init__(self, player_id: _Optional[str] = ..., nickname: _Optional[str] = ..., level: _Optional[int] = ..., class_id: _Optional[str] = ..., rank: _Optional[int] = ..., score: _Optional[int] = ..., player_storage_entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ...) -> None: ...

class PlayerGrandPrixRankInfo(_message.Message):
    __slots__ = ["player_id", "point", "rank"]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    player_id: str
    point: int
    rank: int
    def __init__(self, player_id: _Optional[str] = ..., rank: _Optional[int] = ..., point: _Optional[int] = ...) -> None: ...

class PlayerGrandPrixRankingInfo(_message.Message):
    __slots__ = ["class_id", "level", "nickname", "player_id", "player_storage_entries", "point", "rank"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STORAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    level: int
    nickname: str
    player_id: str
    player_storage_entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
    point: int
    rank: int
    def __init__(self, player_id: _Optional[str] = ..., nickname: _Optional[str] = ..., level: _Optional[int] = ..., class_id: _Optional[str] = ..., rank: _Optional[int] = ..., point: _Optional[int] = ..., player_storage_entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ...) -> None: ...

class PlayerPeriodClassPrizeInfo(_message.Message):
    __slots__ = ["class_id", "class_inventories", "period_id", "rank", "ranking_inventories"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    PERIOD_ID_FIELD_NUMBER: _ClassVar[int]
    RANKING_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    class_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
    period_id: str
    rank: int
    ranking_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
    def __init__(self, period_id: _Optional[str] = ..., class_id: _Optional[str] = ..., rank: _Optional[int] = ..., ranking_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., class_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ...) -> None: ...

class Prize(_message.Message):
    __slots__ = ["inventory_message", "item_type", "prize_id", "resource_name", "resource_num", "schema_key", "search_label", "value"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIZE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    item_type: _v1_pb2.ItemType
    prize_id: str
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    value: bytes
    def __init__(self, prize_id: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., inventory_message: _Optional[str] = ..., search_label: _Optional[str] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ...) -> None: ...

class RankingPrize(_message.Message):
    __slots__ = ["end_rank", "prizes", "start_rank"]
    END_RANK_FIELD_NUMBER: _ClassVar[int]
    PRIZES_FIELD_NUMBER: _ClassVar[int]
    START_RANK_FIELD_NUMBER: _ClassVar[int]
    end_rank: int
    prizes: _containers.RepeatedCompositeFieldContainer[Prize]
    start_rank: int
    def __init__(self, start_rank: _Optional[int] = ..., end_rank: _Optional[int] = ..., prizes: _Optional[_Iterable[_Union[Prize, _Mapping]]] = ...) -> None: ...

class Season(_message.Message):
    __slots__ = ["closed_at", "entry_opened_at", "finished_at", "opened_at", "period", "ranking_prizes", "season_id"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    RANKING_PRIZES_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    entry_opened_at: int
    finished_at: int
    opened_at: int
    period: Period
    ranking_prizes: _containers.RepeatedCompositeFieldContainer[RankingPrize]
    season_id: str
    def __init__(self, season_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., finished_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., period: _Optional[_Union[Period, _Mapping]] = ..., ranking_prizes: _Optional[_Iterable[_Union[RankingPrize, _Mapping]]] = ..., entry_opened_at: _Optional[int] = ...) -> None: ...
