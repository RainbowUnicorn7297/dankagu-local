from takasho.schema.common_featureset.resource.consume_resource_set import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameProduct(_message.Message):
    __slots__ = ["closed_at", "consume_resource_sets", "game_product_id", "inventory_message", "labels", "opened_at", "receivable_sec", "schema_key", "search_label", "value"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    CONSUME_RESOURCE_SETS_FIELD_NUMBER: _ClassVar[int]
    GAME_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    RECEIVABLE_SEC_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    consume_resource_sets: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ConsumeResourceSet]
    game_product_id: str
    inventory_message: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    opened_at: int
    receivable_sec: int
    schema_key: str
    search_label: str
    value: bytes
    def __init__(self, game_product_id: _Optional[str] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., inventory_message: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., receivable_sec: _Optional[int] = ..., search_label: _Optional[str] = ..., consume_resource_sets: _Optional[_Iterable[_Union[_v1_pb2.ConsumeResourceSet, _Mapping]]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
