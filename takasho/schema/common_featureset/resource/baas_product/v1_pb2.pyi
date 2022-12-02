from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaasProduct(_message.Message):
    __slots__ = ["baas_product_id", "extras", "inventory_message"]
    BAAS_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    baas_product_id: str
    extras: _containers.RepeatedCompositeFieldContainer[BaasProductExtra]
    inventory_message: str
    def __init__(self, baas_product_id: _Optional[str] = ..., inventory_message: _Optional[str] = ..., extras: _Optional[_Iterable[_Union[BaasProductExtra, _Mapping]]] = ...) -> None: ...

class BaasProductExtra(_message.Message):
    __slots__ = ["baas_product_extra_id", "item_type", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value"]
    BAAS_PRODUCT_EXTRA_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    baas_product_extra_id: str
    item_type: _v1_pb2.ItemType
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    def __init__(self, baas_product_extra_id: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ..., search_label: _Optional[str] = ...) -> None: ...
