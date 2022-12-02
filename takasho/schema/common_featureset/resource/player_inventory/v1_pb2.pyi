from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACHIEVEMENT: Route
ASC: OrderDirection
BOX_LOOT_BOX: Route
COMPENSATION: Route
DESC: OrderDirection
DESCRIPTOR: _descriptor.FileDescriptor
EXPIRED_AT: OrderField
GAME_PRODUCT: Route
GAME_RUNTIME: ItemType
LOGIN_BONUS: Route
LOOT_BOX: Route
OPENED_AT: OrderField
PLAYER_KEY_VALUE_STORE: ItemType
PURCHASE: Route
STEP_UP_LOOT_BOX: Route
TOTAL_LOGIN_BONUS: Route
UNKNOWN: Route
VIRTUAL_CURRENCY: ItemType

class Criterion(_message.Message):
    __slots__ = ["count", "expired_at_after", "expired_at_before", "order", "page_token", "routes", "search_labels"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_AFTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABELS_FIELD_NUMBER: _ClassVar[int]
    count: int
    expired_at_after: int
    expired_at_before: int
    order: Order
    page_token: str
    routes: _containers.RepeatedScalarFieldContainer[Route]
    search_labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, count: _Optional[int] = ..., routes: _Optional[_Iterable[_Union[Route, str]]] = ..., search_labels: _Optional[_Iterable[str]] = ..., page_token: _Optional[str] = ..., expired_at_before: _Optional[int] = ..., expired_at_after: _Optional[int] = ..., order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["direction", "field"]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    direction: OrderDirection
    field: OrderField
    def __init__(self, field: _Optional[_Union[OrderField, str]] = ..., direction: _Optional[_Union[OrderDirection, str]] = ...) -> None: ...

class PlayerInventory(_message.Message):
    __slots__ = ["created_at", "expired_at", "id", "item_type", "message", "opened_at", "player_id", "route", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    expired_at: int
    id: str
    item_type: ItemType
    message: str
    opened_at: int
    player_id: str
    route: Route
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    def __init__(self, id: _Optional[str] = ..., player_id: _Optional[str] = ..., item_type: _Optional[_Union[ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., route: _Optional[_Union[Route, str]] = ..., message: _Optional[str] = ..., search_label: _Optional[str] = ..., opened_at: _Optional[int] = ..., expired_at: _Optional[int] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ..., created_at: _Optional[int] = ...) -> None: ...

class ReceivedPlayerInventory(_message.Message):
    __slots__ = ["created_at", "expired_at", "id", "item_type", "message", "opened_at", "original_inventory_id", "player_id", "received_at", "route", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_INVENTORY_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    expired_at: int
    id: str
    item_type: ItemType
    message: str
    opened_at: int
    original_inventory_id: str
    player_id: str
    received_at: int
    route: Route
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    def __init__(self, id: _Optional[str] = ..., original_inventory_id: _Optional[str] = ..., player_id: _Optional[str] = ..., item_type: _Optional[_Union[ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., route: _Optional[_Union[Route, str]] = ..., message: _Optional[str] = ..., search_label: _Optional[str] = ..., opened_at: _Optional[int] = ..., expired_at: _Optional[int] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ..., created_at: _Optional[int] = ..., received_at: _Optional[int] = ...) -> None: ...

class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Route(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OrderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OrderDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
