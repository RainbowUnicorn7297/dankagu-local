from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoxLootBox(_message.Message):
    __slots__ = ["af_box_remain", "exec_num", "gacha_id", "get_item_ids", "paid_amount", "paid_id", "takasho_log", "transaction_id"]
    AF_BOX_REMAIN_FIELD_NUMBER: _ClassVar[int]
    EXEC_NUM_FIELD_NUMBER: _ClassVar[int]
    GACHA_ID_FIELD_NUMBER: _ClassVar[int]
    GET_ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    PAID_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAID_ID_FIELD_NUMBER: _ClassVar[int]
    TAKASHO_LOG_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    af_box_remain: int
    exec_num: int
    gacha_id: str
    get_item_ids: _containers.RepeatedScalarFieldContainer[str]
    paid_amount: int
    paid_id: str
    takasho_log: bytes
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ..., gacha_id: _Optional[str] = ..., exec_num: _Optional[int] = ..., get_item_ids: _Optional[_Iterable[str]] = ..., paid_id: _Optional[str] = ..., paid_amount: _Optional[int] = ..., af_box_remain: _Optional[int] = ..., takasho_log: _Optional[bytes] = ...) -> None: ...

class ConsumeResource(_message.Message):
    __slots__ = ["consume_resource_key", "consume_resource_num"]
    CONSUME_RESOURCE_KEY_FIELD_NUMBER: _ClassVar[int]
    CONSUME_RESOURCE_NUM_FIELD_NUMBER: _ClassVar[int]
    consume_resource_key: str
    consume_resource_num: int
    def __init__(self, consume_resource_key: _Optional[str] = ..., consume_resource_num: _Optional[int] = ...) -> None: ...

class ConsumeVc(_message.Message):
    __slots__ = ["currencies", "id", "takasho_log"]
    class Currency(_message.Message):
        __slots__ = ["amonut", "name"]
        AMONUT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        amonut: int
        name: str
        def __init__(self, name: _Optional[str] = ..., amonut: _Optional[int] = ...) -> None: ...
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TAKASHO_LOG_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[ConsumeVc.Currency]
    id: str
    takasho_log: bytes
    def __init__(self, id: _Optional[str] = ..., currencies: _Optional[_Iterable[_Union[ConsumeVc.Currency, _Mapping]]] = ..., takasho_log: _Optional[bytes] = ...) -> None: ...

class FriendV1(_message.Message):
    __slots__ = ["action_type", "friends_num", "max_friends_num", "takasho_log", "target_player_ids"]
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVE: FriendV1.ActionType
    DELETE_FRIEND: FriendV1.ActionType
    DELETE_SENT_REQUEST: FriendV1.ActionType
    FRIENDS_NUM_FIELD_NUMBER: _ClassVar[int]
    MAX_FRIENDS_NUM_FIELD_NUMBER: _ClassVar[int]
    REJECT: FriendV1.ActionType
    SEND: FriendV1.ActionType
    TAKASHO_LOG_FIELD_NUMBER: _ClassVar[int]
    TARGET_PLAYER_IDS_FIELD_NUMBER: _ClassVar[int]
    action_type: FriendV1.ActionType
    friends_num: int
    max_friends_num: int
    takasho_log: bytes
    target_player_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, action_type: _Optional[_Union[FriendV1.ActionType, str]] = ..., target_player_ids: _Optional[_Iterable[str]] = ..., friends_num: _Optional[int] = ..., max_friends_num: _Optional[int] = ..., takasho_log: _Optional[bytes] = ...) -> None: ...

class LootBoxV3(_message.Message):
    __slots__ = ["consume_resources", "content_ids", "content_values", "loot_box_product_id", "num", "takasho_log", "transaction_id"]
    CONSUME_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_VALUES_FIELD_NUMBER: _ClassVar[int]
    LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    TAKASHO_LOG_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    consume_resources: _containers.RepeatedCompositeFieldContainer[ConsumeResource]
    content_ids: _containers.RepeatedScalarFieldContainer[str]
    content_values: _containers.RepeatedScalarFieldContainer[bytes]
    loot_box_product_id: str
    num: int
    takasho_log: bytes
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ..., loot_box_product_id: _Optional[str] = ..., num: _Optional[int] = ..., content_ids: _Optional[_Iterable[str]] = ..., consume_resources: _Optional[_Iterable[_Union[ConsumeResource, _Mapping]]] = ..., content_values: _Optional[_Iterable[bytes]] = ..., takasho_log: _Optional[bytes] = ...) -> None: ...

class PlayerEventLog(_message.Message):
    __slots__ = ["event_category", "event_id", "payload", "player_state", "player_state_bytes"]
    EVENT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STATE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STATE_FIELD_NUMBER: _ClassVar[int]
    event_category: str
    event_id: str
    payload: bytes
    player_state: str
    player_state_bytes: bytes
    def __init__(self, event_category: _Optional[str] = ..., event_id: _Optional[str] = ..., payload: _Optional[bytes] = ..., player_state: _Optional[str] = ..., player_state_bytes: _Optional[bytes] = ...) -> None: ...

class PlayerEventLogServerPayload(_message.Message):
    __slots__ = ["takasho_log"]
    TAKASHO_LOG_FIELD_NUMBER: _ClassVar[int]
    takasho_log: bytes
    def __init__(self, takasho_log: _Optional[bytes] = ...) -> None: ...

class StepUpLootBoxV2(_message.Message):
    __slots__ = ["consume_resources", "content_ids", "content_values", "next_step", "step", "step_up_loot_box_product_id", "takasho_log", "transaction_id"]
    CONSUME_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_VALUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_STEP_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    TAKASHO_LOG_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    consume_resources: _containers.RepeatedCompositeFieldContainer[ConsumeResource]
    content_ids: _containers.RepeatedScalarFieldContainer[str]
    content_values: _containers.RepeatedScalarFieldContainer[bytes]
    next_step: int
    step: int
    step_up_loot_box_product_id: str
    takasho_log: bytes
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ..., step_up_loot_box_product_id: _Optional[str] = ..., step: _Optional[int] = ..., next_step: _Optional[int] = ..., content_ids: _Optional[_Iterable[str]] = ..., consume_resources: _Optional[_Iterable[_Union[ConsumeResource, _Mapping]]] = ..., content_values: _Optional[_Iterable[bytes]] = ..., takasho_log: _Optional[bytes] = ...) -> None: ...
