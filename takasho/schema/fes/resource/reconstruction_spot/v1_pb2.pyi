from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Prize(_message.Message):
    __slots__ = ["inventory_message", "is_unlocked", "item_type", "prize_id", "ratio", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value", "value_path"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIZE_ID_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PATH_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    is_unlocked: bool
    item_type: _v1_pb2.ItemType
    prize_id: str
    ratio: float
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    value_path: str
    def __init__(self, prize_id: _Optional[str] = ..., ratio: _Optional[float] = ..., item_type: _Optional[_Union[_v1_pb2.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., value_path: _Optional[str] = ..., inventory_message: _Optional[str] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ..., is_unlocked: bool = ...) -> None: ...

class Spot(_message.Message):
    __slots__ = ["closed_at", "finished_at", "key", "opened_at", "spot_id", "stages"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    SPOT_ID_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    finished_at: int
    key: str
    opened_at: int
    spot_id: str
    stages: _containers.RepeatedCompositeFieldContainer[Stage]
    def __init__(self, spot_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., finished_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., key: _Optional[str] = ..., stages: _Optional[_Iterable[_Union[Stage, _Mapping]]] = ...) -> None: ...

class Stage(_message.Message):
    __slots__ = ["aggregated_tickets_count", "closed_at", "max_tickets_count", "opened_at", "prizes", "stage"]
    AGGREGATED_TICKETS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    MAX_TICKETS_COUNT_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PRIZES_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    aggregated_tickets_count: int
    closed_at: int
    max_tickets_count: int
    opened_at: int
    prizes: _containers.RepeatedCompositeFieldContainer[Prize]
    stage: int
    def __init__(self, stage: _Optional[int] = ..., max_tickets_count: _Optional[int] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., prizes: _Optional[_Iterable[_Union[Prize, _Mapping]]] = ..., aggregated_tickets_count: _Optional[int] = ...) -> None: ...
