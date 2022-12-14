from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DATE_LINE: ResetType
DESCRIPTOR: _descriptor.FileDescriptor
TIME_LAPSE: ResetType

class LoginBonus(_message.Message):
    __slots__ = ["closed_at", "date_line", "last_counted_up_at", "last_prize_count", "login_bonus_id", "loop", "opened_at", "prizes", "reset_type", "time_lapse"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    DATE_LINE_FIELD_NUMBER: _ClassVar[int]
    LAST_COUNTED_UP_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_PRIZE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOGIN_BONUS_ID_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PRIZES_FIELD_NUMBER: _ClassVar[int]
    RESET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_LAPSE_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    date_line: str
    last_counted_up_at: int
    last_prize_count: int
    login_bonus_id: str
    loop: bool
    opened_at: int
    prizes: _containers.RepeatedCompositeFieldContainer[LoginBonusPrize]
    reset_type: ResetType
    time_lapse: int
    def __init__(self, login_bonus_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., reset_type: _Optional[_Union[ResetType, str]] = ..., date_line: _Optional[str] = ..., time_lapse: _Optional[int] = ..., last_prize_count: _Optional[int] = ..., last_counted_up_at: _Optional[int] = ..., prizes: _Optional[_Iterable[_Union[LoginBonusPrize, _Mapping]]] = ..., loop: bool = ...) -> None: ...

class LoginBonusPrize(_message.Message):
    __slots__ = ["item_type", "login_bonus_id", "login_bonus_prize_id", "prize_count", "resource_name", "resource_num", "schema_key", "search_label", "value"]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_BONUS_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_BONUS_PRIZE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIZE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    item_type: _v1_pb2.ItemType
    login_bonus_id: str
    login_bonus_prize_id: str
    prize_count: int
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    value: bytes
    def __init__(self, login_bonus_id: _Optional[str] = ..., login_bonus_prize_id: _Optional[str] = ..., prize_count: _Optional[int] = ..., item_type: _Optional[_Union[_v1_pb2.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., search_label: _Optional[str] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ...) -> None: ...

class ResetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
