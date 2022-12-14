from takasho.schema.common_featureset.resource.login_bonus import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BingoLoginBonus(_message.Message):
    __slots__ = ["bingo_login_bonus_id", "bingo_prizes", "bingo_statuses", "closed_at", "count_bingo_rows", "date_line", "last_counted_up_at", "omikuji_prizes", "opened_at", "reset_type", "time_lapse"]
    BINGO_LOGIN_BONUS_ID_FIELD_NUMBER: _ClassVar[int]
    BINGO_PRIZES_FIELD_NUMBER: _ClassVar[int]
    BINGO_STATUSES_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    COUNT_BINGO_ROWS_FIELD_NUMBER: _ClassVar[int]
    DATE_LINE_FIELD_NUMBER: _ClassVar[int]
    LAST_COUNTED_UP_AT_FIELD_NUMBER: _ClassVar[int]
    OMIKUJI_PRIZES_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    RESET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_LAPSE_FIELD_NUMBER: _ClassVar[int]
    bingo_login_bonus_id: str
    bingo_prizes: _containers.RepeatedCompositeFieldContainer[BingoLoginBonusPrize]
    bingo_statuses: _containers.RepeatedCompositeFieldContainer[BingoStatus]
    closed_at: int
    count_bingo_rows: int
    date_line: str
    last_counted_up_at: int
    omikuji_prizes: _containers.RepeatedCompositeFieldContainer[BingoLoginBonusOmikujiPrize]
    opened_at: int
    reset_type: _v1_pb2.ResetType
    time_lapse: int
    def __init__(self, bingo_login_bonus_id: _Optional[str] = ..., reset_type: _Optional[_Union[_v1_pb2.ResetType, str]] = ..., date_line: _Optional[str] = ..., time_lapse: _Optional[int] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., bingo_prizes: _Optional[_Iterable[_Union[BingoLoginBonusPrize, _Mapping]]] = ..., omikuji_prizes: _Optional[_Iterable[_Union[BingoLoginBonusOmikujiPrize, _Mapping]]] = ..., last_counted_up_at: _Optional[int] = ..., bingo_statuses: _Optional[_Iterable[_Union[BingoStatus, _Mapping]]] = ..., count_bingo_rows: _Optional[int] = ...) -> None: ...

class BingoLoginBonusOmikujiPrize(_message.Message):
    __slots__ = ["frame_num", "inventory_message", "item_type", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value", "value_path"]
    FRAME_NUM_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PATH_FIELD_NUMBER: _ClassVar[int]
    frame_num: int
    inventory_message: str
    item_type: _v1_pb2_1.ItemType
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: str
    value_path: str
    def __init__(self, frame_num: _Optional[int] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[str] = ..., value_path: _Optional[str] = ..., inventory_message: _Optional[str] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ...) -> None: ...

class BingoLoginBonusPrize(_message.Message):
    __slots__ = ["inventory_message", "item_type", "row", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value", "value_path"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PATH_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    item_type: _v1_pb2_1.ItemType
    row: int
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: str
    value_path: str
    def __init__(self, row: _Optional[int] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[str] = ..., value_path: _Optional[str] = ..., inventory_message: _Optional[str] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ...) -> None: ...

class BingoStatus(_message.Message):
    __slots__ = ["frame", "is_open"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    frame: int
    is_open: bool
    def __init__(self, frame: _Optional[int] = ..., is_open: bool = ...) -> None: ...
