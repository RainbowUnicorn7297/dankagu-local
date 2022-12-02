from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RenewalCount(_message.Message):
    __slots__ = ["count", "subscription_product_id"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    count: int
    subscription_product_id: str
    def __init__(self, subscription_product_id: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class RenewalReward(_message.Message):
    __slots__ = ["closed_at", "is_loop", "opened_at", "prizes", "reward_id", "subscription_product_id"]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    PRIZES_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    closed_at: int
    is_loop: bool
    opened_at: int
    prizes: _containers.RepeatedCompositeFieldContainer[RenewalRewardPrize]
    reward_id: str
    subscription_product_id: str
    def __init__(self, reward_id: _Optional[str] = ..., subscription_product_id: _Optional[str] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., prizes: _Optional[_Iterable[_Union[RenewalRewardPrize, _Mapping]]] = ..., is_loop: bool = ...) -> None: ...

class RenewalRewardPrize(_message.Message):
    __slots__ = ["count", "item_type", "reward_prize_id", "schema_key", "search_label", "system_resource_name", "system_resource_num", "value"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    REWARD_PRIZE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_KEY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LABEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    count: int
    item_type: _v1_pb2.ItemType
    reward_prize_id: str
    schema_key: str
    search_label: str
    system_resource_name: str
    system_resource_num: int
    value: bytes
    def __init__(self, reward_prize_id: _Optional[str] = ..., count: _Optional[int] = ..., item_type: _Optional[_Union[_v1_pb2.ItemType, str]] = ..., schema_key: _Optional[str] = ..., value: _Optional[bytes] = ..., search_label: _Optional[str] = ..., system_resource_name: _Optional[str] = ..., system_resource_num: _Optional[int] = ...) -> None: ...
