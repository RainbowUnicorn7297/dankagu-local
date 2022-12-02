from takasho.schema.common_featureset.resource.step_up_loot_box import v2_pb2 as _v2_pb2
from takasho.schema.common_featureset.resource.step_up_loot_box import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1_1
from takasho.schema.common_featureset.resource.wallet import v3_pb2 as _v3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StepUpLootBoxGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["max_results", "page_token"]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["next_page_token", "prev_page_token", "step_up_loot_box_products"]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        next_page_token: str
        prev_page_token: str
        step_up_loot_box_products: _containers.RepeatedCompositeFieldContainer[_v1_pb2.StepUpLootBoxProductWithPlayerStepNum]
        def __init__(self, step_up_loot_box_products: _Optional[_Iterable[_Union[_v1_pb2.StepUpLootBoxProductWithPlayerStepNum, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxGetDetailV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["step_up_loot_box_product_id"]
        STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_product_id: str
        def __init__(self, step_up_loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["step_up_loot_box_product"]
        STEP_UP_LOOT_BOX_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_product: _v1_pb2.StepUpLootBoxProductWithPlayerStepNum
        def __init__(self, step_up_loot_box_product: _Optional[_Union[_v1_pb2.StepUpLootBoxProductWithPlayerStepNum, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxGetProbabilityV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["step_up_loot_box_product_id"]
        STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_product_id: str
        def __init__(self, step_up_loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["step_up_loot_box_probability"]
        STEP_UP_LOOT_BOX_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_probability: _v2_pb2.StepUpLootBoxProbability
        def __init__(self, step_up_loot_box_probability: _Optional[_Union[_v2_pb2.StepUpLootBoxProbability, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxPurchaseV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "resource_type", "step_up_loot_box_product_id", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: StepUpLootBoxPurchaseV1.Request.ResourceType
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: StepUpLootBoxPurchaseV1.Request.ResourceType
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        resource_type: StepUpLootBoxPurchaseV1.Request.ResourceType
        step_up_loot_box_product_id: str
        transaction_id: str
        def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., resource_type: _Optional[_Union[StepUpLootBoxPurchaseV1.Request.ResourceType, str]] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["extra_player_inventories", "player_inventories", "step_up_loot_box_contents", "transaction_id", "wallet"]
        EXTRA_PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_CONTENTS_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        extra_player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        step_up_loot_box_contents: _containers.RepeatedCompositeFieldContainer[_v2_pb2.StepUpLootBoxContent]
        transaction_id: str
        wallet: _v3_pb2.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., step_up_loot_box_contents: _Optional[_Iterable[_Union[_v2_pb2.StepUpLootBoxContent, _Mapping]]] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ..., extra_player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxV2GetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["max_results", "page_token"]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["next_page_token", "prev_page_token", "step_up_loot_box_products"]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        next_page_token: str
        prev_page_token: str
        step_up_loot_box_products: _containers.RepeatedCompositeFieldContainer[_v2_pb2.StepUpLootBoxProduct]
        def __init__(self, step_up_loot_box_products: _Optional[_Iterable[_Union[_v2_pb2.StepUpLootBoxProduct, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxV2GetDetailV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["step_up_loot_box_product_ids"]
        STEP_UP_LOOT_BOX_PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_product_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, step_up_loot_box_product_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["step_up_loot_box_products", "step_up_loot_box_specific_content_extras"]
        STEP_UP_LOOT_BOX_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_SPECIFIC_CONTENT_EXTRAS_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_products: _containers.RepeatedCompositeFieldContainer[_v2_pb2.StepUpLootBoxProduct]
        step_up_loot_box_specific_content_extras: _containers.RepeatedCompositeFieldContainer[_v2_pb2.StepUpLootBoxSpecificContentExtra]
        def __init__(self, step_up_loot_box_products: _Optional[_Iterable[_Union[_v2_pb2.StepUpLootBoxProduct, _Mapping]]] = ..., step_up_loot_box_specific_content_extras: _Optional[_Iterable[_Union[_v2_pb2.StepUpLootBoxSpecificContentExtra, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxV2GetProbabilityV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["step_up_loot_box_product_ids"]
        STEP_UP_LOOT_BOX_PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
        step_up_loot_box_product_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, step_up_loot_box_product_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["purchase_token", "step_up_loot_box_probabilities"]
        PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_PROBABILITIES_FIELD_NUMBER: _ClassVar[int]
        purchase_token: str
        step_up_loot_box_probabilities: _containers.RepeatedCompositeFieldContainer[_v2_pb2.StepUpLootBoxProbability]
        def __init__(self, step_up_loot_box_probabilities: _Optional[_Iterable[_Union[_v2_pb2.StepUpLootBoxProbability, _Mapping]]] = ..., purchase_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class StepUpLootBoxV2PurchaseV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "purchase_token", "resource_type", "step_up_loot_box_product_id", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: StepUpLootBoxV2PurchaseV1.Request.ResourceType
        PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: StepUpLootBoxV2PurchaseV1.Request.ResourceType
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        purchase_token: str
        resource_type: StepUpLootBoxV2PurchaseV1.Request.ResourceType
        step_up_loot_box_product_id: str
        transaction_id: str
        def __init__(self, step_up_loot_box_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., resource_type: _Optional[_Union[StepUpLootBoxV2PurchaseV1.Request.ResourceType, str]] = ..., purchase_token: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["extra_player_inventories", "player_inventories", "specific_content_extras", "step_up_loot_box_contents", "transaction_id", "wallet"]
        EXTRA_PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        SPECIFIC_CONTENT_EXTRAS_FIELD_NUMBER: _ClassVar[int]
        STEP_UP_LOOT_BOX_CONTENTS_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        extra_player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        specific_content_extras: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        step_up_loot_box_contents: _containers.RepeatedCompositeFieldContainer[_v2_pb2.StepUpLootBoxContent]
        transaction_id: str
        wallet: _v3_pb2.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., step_up_loot_box_contents: _Optional[_Iterable[_Union[_v2_pb2.StepUpLootBoxContent, _Mapping]]] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ..., extra_player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ..., specific_content_extras: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
