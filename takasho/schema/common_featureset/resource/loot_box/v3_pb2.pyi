from takasho.schema.common_featureset.resource.consume_resource_set import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DATE_LINE: LimitType
DESCRIPTOR: _descriptor.FileDescriptor
NONE: LimitType
TOTAL: LimitType

class Extra(_message.Message):
    __slots__ = ["inventory_message", "is_receive_directly", "item_type", "loot_box_extra_id", "resource_name", "resource_num", "schema_key", "search_label", "value"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_RECEIVE_DIRECTLY_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_EXTRA_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    is_receive_directly: bool
    item_type: _v1_pb2_1.ItemType
    loot_box_extra_id: str
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    value: bytes
    def __init__(self, loot_box_extra_id: _Optional[str] = ..., inventory_message: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ..., search_label: _Optional[str] = ..., is_receive_directly: bool = ...) -> None: ...

class Limit(_message.Message):
    __slots__ = ["date_line", "limit_num", "limit_type"]
    DATE_LINE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_NUM_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    date_line: str
    limit_num: int
    limit_type: LimitType
    def __init__(self, limit_type: _Optional[_Union[LimitType, str]] = ..., limit_num: _Optional[int] = ..., date_line: _Optional[str] = ...) -> None: ...

class LootBoxContent(_message.Message):
    __slots__ = ["item_type", "loot_box_content_id", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value", "weight"]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    item_type: _v1_pb2_1.ItemType
    loot_box_content_id: str
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    weight: int
    def __init__(self, loot_box_content_id: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., weight: _Optional[int] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ...) -> None: ...

class LootBoxContentProbabilityInContentSet(_message.Message):
    __slots__ = ["loot_box_content_id", "probability", "value"]
    LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    loot_box_content_id: str
    probability: str
    value: bytes
    def __init__(self, loot_box_content_id: _Optional[str] = ..., value: _Optional[bytes] = ..., probability: _Optional[str] = ...) -> None: ...

class LootBoxContentProbabilityInLabel(_message.Message):
    __slots__ = ["loot_box_content_id", "probability", "value"]
    LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    loot_box_content_id: str
    probability: str
    value: bytes
    def __init__(self, loot_box_content_id: _Optional[str] = ..., value: _Optional[bytes] = ..., probability: _Optional[str] = ...) -> None: ...

class LootBoxContentSet(_message.Message):
    __slots__ = ["labels", "loot_box_content_set_id", "lot_num"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    LOT_NUM_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[LootBoxLabel]
    loot_box_content_set_id: str
    lot_num: int
    def __init__(self, loot_box_content_set_id: _Optional[str] = ..., lot_num: _Optional[int] = ..., labels: _Optional[_Iterable[_Union[LootBoxLabel, _Mapping]]] = ...) -> None: ...

class LootBoxContentSetPrizes(_message.Message):
    __slots__ = ["loot_box_content_set_id", "loot_box_contents"]
    LOOT_BOX_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    loot_box_content_set_id: str
    loot_box_contents: _containers.RepeatedCompositeFieldContainer[LootBoxContent]
    def __init__(self, loot_box_content_set_id: _Optional[str] = ..., loot_box_contents: _Optional[_Iterable[_Union[LootBoxContent, _Mapping]]] = ...) -> None: ...

class LootBoxContentSetProbability(_message.Message):
    __slots__ = ["loot_box_content_probabilities_in_content_set", "loot_box_content_set_id", "loot_box_label_probabilities"]
    LOOT_BOX_CONTENT_PROBABILITIES_IN_CONTENT_SET_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_LABEL_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    loot_box_content_probabilities_in_content_set: _containers.RepeatedCompositeFieldContainer[LootBoxContentProbabilityInContentSet]
    loot_box_content_set_id: str
    loot_box_label_probabilities: _containers.RepeatedCompositeFieldContainer[LootBoxLabelProbability]
    def __init__(self, loot_box_content_set_id: _Optional[str] = ..., loot_box_label_probabilities: _Optional[_Iterable[_Union[LootBoxLabelProbability, _Mapping]]] = ..., loot_box_content_probabilities_in_content_set: _Optional[_Iterable[_Union[LootBoxContentProbabilityInContentSet, _Mapping]]] = ...) -> None: ...

class LootBoxLabel(_message.Message):
    __slots__ = ["contents", "loot_box_label", "weight"]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_LABEL_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedCompositeFieldContainer[LootBoxContent]
    loot_box_label: str
    weight: int
    def __init__(self, loot_box_label: _Optional[str] = ..., weight: _Optional[int] = ..., contents: _Optional[_Iterable[_Union[LootBoxContent, _Mapping]]] = ...) -> None: ...

class LootBoxLabelProbability(_message.Message):
    __slots__ = ["label", "loot_box_content_probabilities_in_label", "probability"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_CONTENT_PROBABILITIES_IN_LABEL_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    label: str
    loot_box_content_probabilities_in_label: _containers.RepeatedCompositeFieldContainer[LootBoxContentProbabilityInLabel]
    probability: str
    def __init__(self, label: _Optional[str] = ..., probability: _Optional[str] = ..., loot_box_content_probabilities_in_label: _Optional[_Iterable[_Union[LootBoxContentProbabilityInLabel, _Mapping]]] = ...) -> None: ...

class LootBoxPickup(_message.Message):
    __slots__ = ["loot_box_pickup_id", "pickup_contents", "pickup_extras"]
    LOOT_BOX_PICKUP_ID_FIELD_NUMBER: _ClassVar[int]
    PICKUP_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    PICKUP_EXTRAS_FIELD_NUMBER: _ClassVar[int]
    loot_box_pickup_id: str
    pickup_contents: _containers.RepeatedCompositeFieldContainer[LootBoxContent]
    pickup_extras: _containers.RepeatedCompositeFieldContainer[PickupExtra]
    def __init__(self, loot_box_pickup_id: _Optional[str] = ..., pickup_contents: _Optional[_Iterable[_Union[LootBoxContent, _Mapping]]] = ..., pickup_extras: _Optional[_Iterable[_Union[PickupExtra, _Mapping]]] = ...) -> None: ...

class LootBoxProbability(_message.Message):
    __slots__ = ["loot_box_content_set_probabilities", "loot_box_product_id"]
    LOOT_BOX_CONTENT_SET_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    loot_box_content_set_probabilities: _containers.RepeatedCompositeFieldContainer[LootBoxContentSetProbability]
    loot_box_product_id: str
    def __init__(self, loot_box_product_id: _Optional[str] = ..., loot_box_content_set_probabilities: _Optional[_Iterable[_Union[LootBoxContentSetProbability, _Mapping]]] = ...) -> None: ...

class LootBoxProduct(_message.Message):
    __slots__ = ["closed_at", "consume_resource_sets", "extras", "has_extra", "has_limit", "inventory_message", "limit", "loot_box_product_id", "opened_at", "total_lot_num"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    CONSUME_RESOURCE_SETS_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    HAS_EXTRA_FIELD_NUMBER: _ClassVar[int]
    HAS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOT_NUM_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    consume_resource_sets: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ConsumeResourceSet]
    extras: _containers.RepeatedCompositeFieldContainer[Extra]
    has_extra: bool
    has_limit: bool
    inventory_message: str
    limit: Limit
    loot_box_product_id: str
    opened_at: int
    total_lot_num: int
    def __init__(self, loot_box_product_id: _Optional[str] = ..., inventory_message: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., has_extra: bool = ..., extras: _Optional[_Iterable[_Union[Extra, _Mapping]]] = ..., has_limit: bool = ..., limit: _Optional[_Union[Limit, _Mapping]] = ..., total_lot_num: _Optional[int] = ..., consume_resource_sets: _Optional[_Iterable[_Union[_v1_pb2.ConsumeResourceSet, _Mapping]]] = ...) -> None: ...

class LootBoxProductWithPurchasedCount(_message.Message):
    __slots__ = ["is_limited", "loot_box_pickups", "loot_product", "purchased_count"]
    IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_PICKUPS_FIELD_NUMBER: _ClassVar[int]
    LOOT_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_COUNT_FIELD_NUMBER: _ClassVar[int]
    is_limited: bool
    loot_box_pickups: _containers.RepeatedCompositeFieldContainer[LootBoxPickup]
    loot_product: LootBoxProduct
    purchased_count: int
    def __init__(self, loot_product: _Optional[_Union[LootBoxProduct, _Mapping]] = ..., purchased_count: _Optional[int] = ..., is_limited: bool = ..., loot_box_pickups: _Optional[_Iterable[_Union[LootBoxPickup, _Mapping]]] = ...) -> None: ...

class PickupExtra(_message.Message):
    __slots__ = ["inventory_message", "item_type", "loot_box_pickup_extra_id", "resource_name", "resource_num", "schema_key", "search_label", "value"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_PICKUP_EXTRA_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    item_type: _v1_pb2_1.ItemType
    loot_box_pickup_extra_id: str
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    value: bytes
    def __init__(self, loot_box_pickup_extra_id: _Optional[str] = ..., inventory_message: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ..., search_label: _Optional[str] = ...) -> None: ...

class LimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
