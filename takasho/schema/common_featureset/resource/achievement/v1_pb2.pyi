from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DATE_LINE: ResetType
DESCRIPTOR: _descriptor.FileDescriptor
NONE: ResetType
WEEK_LINE: ResetType

class Achievement(_message.Message):
    __slots__ = ["achievement_id", "category", "closed_at", "date_line", "day_of_week", "opened_at", "prizes", "reset_type", "unlock", "value"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    DATE_LINE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PRIZES_FIELD_NUMBER: _ClassVar[int]
    RESET_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    category: str
    closed_at: int
    date_line: str
    day_of_week: int
    opened_at: int
    prizes: _containers.RepeatedCompositeFieldContainer[AchievementPrize]
    reset_type: ResetType
    unlock: bool
    value: bytes
    def __init__(self, achievement_id: _Optional[str] = ..., value: _Optional[bytes] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., reset_type: _Optional[_Union[ResetType, str]] = ..., date_line: _Optional[str] = ..., day_of_week: _Optional[int] = ..., prizes: _Optional[_Iterable[_Union[AchievementPrize, _Mapping]]] = ..., category: _Optional[str] = ..., unlock: bool = ...) -> None: ...

class AchievementPrize(_message.Message):
    __slots__ = ["achievement_id", "achievement_prize_id", "item_type", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_PRIZE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    achievement_prize_id: str
    item_type: _v1_pb2.ItemType
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    def __init__(self, achievement_id: _Optional[str] = ..., achievement_prize_id: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ...) -> None: ...

class Criterion(_message.Message):
    __slots__ = ["category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: str
    def __init__(self, category: _Optional[str] = ...) -> None: ...

class ResetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
