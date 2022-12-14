from takasho.schema.common_featureset.resource.login_bonus import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComebackLoginBonus(_message.Message):
    __slots__ = ["closed_at", "comeback_login_bonus_id", "comeback_login_bonus_prizes", "condition_days", "date_line", "last_counted_up_at", "opened_at", "reset_type", "time_lapse", "valid_days"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    COMEBACK_LOGIN_BONUS_ID_FIELD_NUMBER: _ClassVar[int]
    COMEBACK_LOGIN_BONUS_PRIZES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_DAYS_FIELD_NUMBER: _ClassVar[int]
    DATE_LINE_FIELD_NUMBER: _ClassVar[int]
    LAST_COUNTED_UP_AT_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    RESET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_LAPSE_FIELD_NUMBER: _ClassVar[int]
    VALID_DAYS_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    comeback_login_bonus_id: str
    comeback_login_bonus_prizes: _containers.RepeatedCompositeFieldContainer[ComebackLoginBonusPrize]
    condition_days: int
    date_line: str
    last_counted_up_at: int
    opened_at: int
    reset_type: _v1_pb2.ResetType
    time_lapse: int
    valid_days: int
    def __init__(self, comeback_login_bonus_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., condition_days: _Optional[int] = ..., valid_days: _Optional[int] = ..., reset_type: _Optional[_Union[_v1_pb2.ResetType, str]] = ..., date_line: _Optional[str] = ..., time_lapse: _Optional[int] = ..., comeback_login_bonus_prizes: _Optional[_Iterable[_Union[ComebackLoginBonusPrize, _Mapping]]] = ..., last_counted_up_at: _Optional[int] = ...) -> None: ...

class ComebackLoginBonusPrize(_message.Message):
    __slots__ = ["days", "inventory_message", "item_type", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value", "value_path"]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PATH_FIELD_NUMBER: _ClassVar[int]
    days: int
    inventory_message: str
    item_type: _v1_pb2_1.ItemType
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: str
    value_path: str
    def __init__(self, days: _Optional[int] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[str] = ..., value_path: _Optional[str] = ..., inventory_message: _Optional[str] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ...) -> None: ...

class ComebackLoginBonusProgress(_message.Message):
    __slots__ = ["come_backed_at", "expired_at", "player_id", "remain_days"]
    COME_BACKED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    REMAIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    come_backed_at: int
    expired_at: int
    player_id: str
    remain_days: int
    def __init__(self, player_id: _Optional[str] = ..., remain_days: _Optional[int] = ..., come_backed_at: _Optional[int] = ..., expired_at: _Optional[int] = ...) -> None: ...
