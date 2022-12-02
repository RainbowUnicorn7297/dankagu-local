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

class SpecificContentExtra(_message.Message):
    __slots__ = ["inventory_message", "item_type", "resource_name", "resource_num", "schema_key", "search_label", "specific_content_extra_id", "value"]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_CONTENT_EXTRA_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventory_message: str
    item_type: _v1_pb2_1.ItemType
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    specific_content_extra_id: str
    value: bytes
    def __init__(self, specific_content_extra_id: _Optional[str] = ..., inventory_message: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ..., search_label: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContent(_message.Message):
    __slots__ = ["item_type", "resource_name", "resource_num", "schema_key", "search_label", "step_up_loot_box_content_id", "value", "weight"]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    item_type: _v1_pb2_1.ItemType
    resource_name: str
    resource_num: int
    schema_key: str
    search_label: str
    step_up_loot_box_content_id: str
    value: bytes
    weight: int
    def __init__(self, step_up_loot_box_content_id: _Optional[str] = ..., item_type: _Optional[_Union[_v1_pb2_1.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., weight: _Optional[int] = ..., resource_name: _Optional[str] = ..., resource_num: _Optional[int] = ..., search_label: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContentProbabilityInContentSet(_message.Message):
    __slots__ = ["probability", "schema_key", "step_up_loot_box_content_id", "value"]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    probability: str
    schema_key: str
    step_up_loot_box_content_id: str
    value: bytes
    def __init__(self, step_up_loot_box_content_id: _Optional[str] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., probability: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContentProbabilityInLabel(_message.Message):
    __slots__ = ["probability", "schema_key", "step_up_loot_box_content_id", "value"]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    probability: str
    schema_key: str
    step_up_loot_box_content_id: str
    value: bytes
    def __init__(self, step_up_loot_box_content_id: _Optional[str] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., probability: _Optional[str] = ...) -> None: ...

class StepUpLootBoxContentSet(_message.Message):
    __slots__ = ["labels", "lot_num", "step_up_loot_box_content_set_id"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOT_NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxLabel]
    lot_num: int
    step_up_loot_box_content_set_id: str
    def __init__(self, step_up_loot_box_content_set_id: _Optional[str] = ..., lot_num: _Optional[int] = ..., labels: _Optional[_Iterable[_Union[StepUpLootBoxLabel, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxContentSetProbability(_message.Message):
    __slots__ = ["lot_num", "step_up_loot_box_content_probabilities_in_content_set", "step_up_loot_box_content_set_id", "step_up_loot_box_label_probabilities"]
    LOT_NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_PROBABILITIES_IN_CONTENT_SET_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_LABEL_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    lot_num: int
    step_up_loot_box_content_probabilities_in_content_set: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentProbabilityInContentSet]
    step_up_loot_box_content_set_id: str
    step_up_loot_box_label_probabilities: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxLabelProbability]
    def __init__(self, step_up_loot_box_content_set_id: _Optional[str] = ..., lot_num: _Optional[int] = ..., step_up_loot_box_label_probabilities: _Optional[_Iterable[_Union[StepUpLootBoxLabelProbability, _Mapping]]] = ..., step_up_loot_box_content_probabilities_in_content_set: _Optional[_Iterable[_Union[StepUpLootBoxContentProbabilityInContentSet, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxLabel(_message.Message):
    __slots__ = ["contents", "step_up_loot_box_label", "weight"]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_LABEL_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContent]
    step_up_loot_box_label: str
    weight: int
    def __init__(self, step_up_loot_box_label: _Optional[str] = ..., weight: _Optional[int] = ..., contents: _Optional[_Iterable[_Union[StepUpLootBoxContent, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxLabelProbability(_message.Message):
    __slots__ = ["label", "probability", "step_up_loot_box_content_probabilities_in_label"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_PROBABILITIES_IN_LABEL_FIELD_NUMBER: _ClassVar[int]
    label: str
    probability: str
    step_up_loot_box_content_probabilities_in_label: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentProbabilityInLabel]
    def __init__(self, label: _Optional[str] = ..., probability: _Optional[str] = ..., step_up_loot_box_content_probabilities_in_label: _Optional[_Iterable[_Union[StepUpLootBoxContentProbabilityInLabel, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxProbability(_message.Message):
    __slots__ = ["step_up_loot_box_product_id", "step_up_loot_box_step_probabilities"]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    step_up_loot_box_product_id: str
    step_up_loot_box_step_probabilities: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxStepProbability]
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., step_up_loot_box_step_probabilities: _Optional[_Iterable[_Union[StepUpLootBoxStepProbability, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxProduct(_message.Message):
    __slots__ = ["closed_at", "is_loop", "loop_times", "next_step_num", "next_step_repeat_times", "opened_at", "step_up_loot_box_product_id", "step_up_loot_box_steps"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    LOOP_TIMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    NEXT_STEP_REPEAT_TIMES_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEPS_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    is_loop: bool
    loop_times: int
    next_step_num: int
    next_step_repeat_times: int
    opened_at: int
    step_up_loot_box_product_id: str
    step_up_loot_box_steps: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxStep]
    def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., is_loop: bool = ..., loop_times: _Optional[int] = ..., step_up_loot_box_steps: _Optional[_Iterable[_Union[StepUpLootBoxStep, _Mapping]]] = ..., next_step_num: _Optional[int] = ..., next_step_repeat_times: _Optional[int] = ...) -> None: ...

class StepUpLootBoxSpecificContentExtra(_message.Message):
    __slots__ = ["extras", "step_up_loot_box_content_id"]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    extras: _containers.RepeatedCompositeFieldContainer[SpecificContentExtra]
    step_up_loot_box_content_id: str
    def __init__(self, step_up_loot_box_content_id: _Optional[str] = ..., extras: _Optional[_Iterable[_Union[SpecificContentExtra, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxStep(_message.Message):
    __slots__ = ["consume_resource_sets", "extras", "has_extra", "inventory_message", "repeat_times", "step_up_loot_box_content_sets", "step_up_loot_box_step_num"]
    CONSUME_RESOURCE_SETS_FIELD_NUMBER: _ClassVar[int]
    EXTRAS_FIELD_NUMBER: _ClassVar[int]
    HAS_EXTRA_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEAT_TIMES_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SETS_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    consume_resource_sets: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ConsumeResourceSet]
    extras: _containers.RepeatedCompositeFieldContainer[Extra]
    has_extra: bool
    inventory_message: str
    repeat_times: int
    step_up_loot_box_content_sets: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentSet]
    step_up_loot_box_step_num: int
    def __init__(self, step_up_loot_box_step_num: _Optional[int] = ..., inventory_message: _Optional[str] = ..., has_extra: bool = ..., extras: _Optional[_Iterable[_Union[Extra, _Mapping]]] = ..., repeat_times: _Optional[int] = ..., step_up_loot_box_content_sets: _Optional[_Iterable[_Union[StepUpLootBoxContentSet, _Mapping]]] = ..., consume_resource_sets: _Optional[_Iterable[_Union[_v1_pb2.ConsumeResourceSet, _Mapping]]] = ...) -> None: ...

class StepUpLootBoxStepProbability(_message.Message):
    __slots__ = ["step_num", "step_up_loot_box_content_set_probabilities"]
    STEP_NUM_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_CONTENT_SET_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
    step_num: int
    step_up_loot_box_content_set_probabilities: _containers.RepeatedCompositeFieldContainer[StepUpLootBoxContentSetProbability]
    def __init__(self, step_num: _Optional[int] = ..., step_up_loot_box_content_set_probabilities: _Optional[_Iterable[_Union[StepUpLootBoxContentSetProbability, _Mapping]]] = ...) -> None: ...
