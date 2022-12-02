from takasho.schema.common_featureset.resource.consume_resource_set import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Extra(_message.Message):
    __slots__ = ["inventory_message", "item_type", "resource_name", "resource_num", "schema_key", "search_label", "step_up_loot_box_extra_id", "value"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_EXTRA_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    item_type: _v1_pb2_1.ItemType
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    step_up_loot_box_extra_id: str
    value: bytes
    def __init__(self, step_up_loot_box_extra_id: _Optional[str] = ..., inventory_message: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ..., search_label: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContent(_message.Message):
    __slots__ = ["item_type", "label", "schema_key", "search_label", "step_up_loot_box_content_id", "step_up_loot_box_content_set_id", "step_up_loot_box_product_id", "step_up_loot_box_step_num", "value", "weight"]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    item_type: _v1_pb2_1.ItemType
    label: str
    schema_key: str
    search_label: str
    step_up_loot_box_content_id: str
    step_up_loot_box_content_set_id: str
    step_up_loot_box_product_id: str
    step_up_loot_box_step_num: int
    value: bytes
    weight: int
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., step_up_loot_box_step_num: _Optional[int] = ..., step_up_loot_box_content_set_id: _Optional[str] = ..., step_up_loot_box_content_id: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., weight: _Optional[int] = ..., label: _Optional[str] = ..., search_label: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContentProbability(_message.Message):
    __slots__ = ["probability", "step_up_loot_box_content_id", "value"]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    probability: str
    step_up_loot_box_content_id: str
    value: bytes
    def __init__(self, step_up_loot_box_content_id: _Optional[str] = ..., value: _Optional[bytes] = ..., probability: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContentSet(_message.Message):
    __slots__ = ["contents", "lot_num", "step_up_loot_box_content_set_id", "step_up_loot_box_product_id", "step_up_loot_box_step_num"]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    LOT_NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContent]
    lot_num: int
    step_up_loot_box_content_set_id: str
    step_up_loot_box_product_id: str
    step_up_loot_box_step_num: int
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., step_up_loot_box_step_num: _Optional[int] = ..., step_up_loot_box_content_set_id: _Optional[str] = ..., lot_num: _Optional[int] = ..., contents: _Optional[_Iterable[_Union[StepUpLootBoxContent, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxContentSetProbability(_message.Message):
    __slots__ = ["step_up_loot_box_content_probabilities", "step_up_loot_box_content_set_id", "step_up_loot_box_label_probability"]
    STEP_UP_LOOT_BOX_CONTENT_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_LABEL_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    step_up_loot_box_content_probabilities: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentProbability]
    step_up_loot_box_content_set_id: str
    step_up_loot_box_label_probability: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxLabelProbability]
    def __init__(self, step_up_loot_box_content_set_id: _Optional[str] = ..., step_up_loot_box_content_probabilities: _Optional[_Iterable[_Union[StepUpLootBoxContentProbability, _Mapping]]] = ..., step_up_loot_box_label_probability: _Optional[_Iterable[_Union[StepUpLootBoxLabelProbability, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxLabelProbability(_message.Message):
    __slots__ = ["label", "probability"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    label: str
    probability: str
    def __init__(self, label: _Optional[str] = ..., probability: _Optional[str] = ...) -> None: ...

class StepUpLootBoxProbability(_message.Message):
    __slots__ = ["step_up_loot_box_product_id", "step_up_loot_box_step_probabilities"]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    step_up_loot_box_product_id: str
    step_up_loot_box_step_probabilities: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxStepProbability]
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., step_up_loot_box_step_probabilities: _Optional[_Iterable[_Union[StepUpLootBoxStepProbability, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxProduct(_message.Message):
    __slots__ = ["closed_at", "is_loop", "opened_at", "step_up_loot_box_product_id", "step_up_loot_box_steps"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEPS_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    is_loop: bool
    opened_at: int
    step_up_loot_box_product_id: str
    step_up_loot_box_steps: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxStep]
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., is_loop: bool = ..., step_up_loot_box_steps: _Optional[_Iterable[_Union[StepUpLootBoxStep, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxProductWithPlayerStepNum(_message.Message):
    __slots__ = ["player_step_num", "product"]
    PLAYER_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    player_step_num: int
    product: StepUpLootBoxProduct
    def __init__(self, product: _Optional[_Union[StepUpLootBoxProduct, _Mapping]] = ..., player_step_num: _Optional[int] = ...) -> None: ...

class StepUpLootBoxStep(_message.Message):
    __slots__ = ["consume_resource_sets", "extras", "has_extra", "inventory_message", "repeat_num", "step_up_loot_box_content_sets", "step_up_loot_box_product_id", "step_up_loot_box_step_num", "total_lot_num"]
    CONSUME_RESOURCE_SETS_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    HAS_EXTRA_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEAT_NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SETS_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOT_NUM_FIELD_NUMBER: _ClassVar[int]
    consume_resource_sets: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ConsumeResourceSet]
    extras: _containers.RepeatedCompositeFieldContainer[Extra]
    has_extra: bool
    inventory_message: str
    repeat_num: int
    step_up_loot_box_content_sets: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentSet]
    step_up_loot_box_product_id: str
    step_up_loot_box_step_num: int
    total_lot_num: int
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., step_up_loot_box_step_num: _Optional[int] = ..., inventory_message: _Optional[str] = ..., has_extra: bool = ..., extras: _Optional[_Iterable[_Union[Extra, _Mapping]]] = ..., repeat_num: _Optional[int] = ..., total_lot_num: _Optional[int] = ..., step_up_loot_box_content_sets: _Optional[_Iterable[_Union[StepUpLootBoxContentSet, _Mapping]]] = ..., consume_resource_sets: _Optional[_Iterable[_Union[_v1_pb2.ConsumeResourceSet, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxStepProbability(_message.Message):
    __slots__ = ["step_up_loot_box_content_set_probabilities", "step_up_loot_box_step_num"]
    STEP_UP_LOOT_BOX_CONTENT_SET_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    step_up_loot_box_content_set_probabilities: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentSetProbability]
    step_up_loot_box_step_num: int
    def __init__(self, step_up_loot_box_step_num: _Optional[int] = ..., step_up_loot_box_content_set_probabilities: _Optional[_Iterable[_Union[StepUpLootBoxContentSetProbability, _Mapping]]] = ...) -> None: ...
