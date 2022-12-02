from takasho.schema.common_featureset.resource.loot_box import v3_pb2 as _v3_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.wallet import v3_pb2 as _v3_pb2_1
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LootBoxGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_products"]
        LOOT_BOX_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        loot_box_products: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxProduct]
        def __init__(self, loot_box_products: _Optional[_Iterable[_Union[_v3_pb2.LootBoxProduct, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxGetDetailV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["is_limited", "loot_box_content_sets", "loot_box_product", "purchasable_count"]
        IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_CONTENT_SETS_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PURCHASABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
        is_limited: bool
        loot_box_content_sets: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxContentSet]
        loot_box_product: _v3_pb2.LootBoxProduct
        purchasable_count: int
        def __init__(self, loot_box_product: _Optional[_Union[_v3_pb2.LootBoxProduct, _Mapping]] = ..., loot_box_content_sets: _Optional[_Iterable[_Union[_v3_pb2.LootBoxContentSet, _Mapping]]] = ..., is_limited: bool = ..., purchasable_count: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxGetProbabilityV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_probability"]
        LOOT_BOX_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
        loot_box_probability: _v3_pb2.LootBoxProbability
        def __init__(self, loot_box_probability: _Optional[_Union[_v3_pb2.LootBoxProbability, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxPurchaseV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id", "transaction_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        transaction_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_contents", "player_inventories", "transaction_id", "wallet"]
        LOOT_BOX_CONTENTS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        loot_box_contents: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxContent]
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        transaction_id: str
        wallet: _v3_pb2_1.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., loot_box_contents: _Optional[_Iterable[_Union[_v3_pb2.LootBoxContent, _Mapping]]] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., wallet: _Optional[_Union[_v3_pb2_1.Wallet, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV2GetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["max_results", "page_token"]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_products", "next_page_token", "prev_page_token"]
        LOOT_BOX_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        loot_box_products: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxProductWithPurchasedCount]
        next_page_token: str
        prev_page_token: str
        def __init__(self, loot_box_products: _Optional[_Iterable[_Union[_v3_pb2.LootBoxProductWithPurchasedCount, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV2GetDetailV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["is_limited", "loot_box_content_sets", "loot_box_pickup", "loot_box_product", "purchased_count"]
        IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_CONTENT_SETS_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_PICKUP_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PURCHASED_COUNT_FIELD_NUMBER: _ClassVar[int]
        is_limited: bool
        loot_box_content_sets: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxContentSet]
        loot_box_pickup: _v3_pb2.LootBoxPickup
        loot_box_product: _v3_pb2.LootBoxProduct
        purchased_count: int
        def __init__(self, loot_box_product: _Optional[_Union[_v3_pb2.LootBoxProduct, _Mapping]] = ..., loot_box_content_sets: _Optional[_Iterable[_Union[_v3_pb2.LootBoxContentSet, _Mapping]]] = ..., is_limited: bool = ..., purchased_count: _Optional[int] = ..., loot_box_pickup: _Optional[_Union[_v3_pb2.LootBoxPickup, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV2GetProbabilityV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_probability"]
        LOOT_BOX_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
        loot_box_probability: _v3_pb2.LootBoxProbability
        def __init__(self, loot_box_probability: _Optional[_Union[_v3_pb2.LootBoxProbability, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV2PurchaseV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id", "resource_type", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: LootBoxV2PurchaseV1.Request.ResourceType
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: LootBoxV2PurchaseV1.Request.ResourceType
        loot_box_product_id: str
        resource_type: LootBoxV2PurchaseV1.Request.ResourceType
        transaction_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., resource_type: _Optional[_Union[LootBoxV2PurchaseV1.Request.ResourceType, str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["extra_player_inventories", "loot_box_content_set_prizes", "pickup_extra_player_inventories", "player_inventories", "transaction_id", "wallet"]
        EXTRA_PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_CONTENT_SET_PRIZES_FIELD_NUMBER: _ClassVar[int]
        PICKUP_EXTRA_PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        extra_player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        loot_box_content_set_prizes: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxContentSetPrizes]
        pickup_extra_player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        transaction_id: str
        wallet: _v3_pb2_1.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., loot_box_content_set_prizes: _Optional[_Iterable[_Union[_v3_pb2.LootBoxContentSetPrizes, _Mapping]]] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., extra_player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., wallet: _Optional[_Union[_v3_pb2_1.Wallet, _Mapping]] = ..., pickup_extra_player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV3GetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["exclude_pickup_response", "max_results", "page_token"]
        EXCLUDE_PICKUP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        exclude_pickup_response: bool
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ..., exclude_pickup_response: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_products", "next_page_token", "prev_page_token"]
        LOOT_BOX_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        loot_box_products: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxProductWithPurchasedCount]
        next_page_token: str
        prev_page_token: str
        def __init__(self, loot_box_products: _Optional[_Iterable[_Union[_v3_pb2.LootBoxProductWithPurchasedCount, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV3GetDetailV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["is_limited", "loot_box_content_sets", "loot_box_pickup", "loot_box_product", "purchased_count"]
        IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_CONTENT_SETS_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_PICKUP_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PURCHASED_COUNT_FIELD_NUMBER: _ClassVar[int]
        is_limited: bool
        loot_box_content_sets: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxContentSet]
        loot_box_pickup: _v3_pb2.LootBoxPickup
        loot_box_product: _v3_pb2.LootBoxProduct
        purchased_count: int
        def __init__(self, loot_box_product: _Optional[_Union[_v3_pb2.LootBoxProduct, _Mapping]] = ..., loot_box_content_sets: _Optional[_Iterable[_Union[_v3_pb2.LootBoxContentSet, _Mapping]]] = ..., is_limited: bool = ..., purchased_count: _Optional[int] = ..., loot_box_pickup: _Optional[_Union[_v3_pb2.LootBoxPickup, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV3GetProbabilityV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id"]
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        loot_box_product_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["loot_box_probability", "purchase_token"]
        LOOT_BOX_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        loot_box_probability: _v3_pb2.LootBoxProbability
        purchase_token: str
        def __init__(self, loot_box_probability: _Optional[_Union[_v3_pb2.LootBoxProbability, _Mapping]] = ..., purchase_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LootBoxV3PurchaseV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["loot_box_product_id", "player_event_logs", "purchase_num", "purchase_token", "resource_type", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        LOOT_BOX_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        NO_CONSUME: LootBoxV3PurchaseV1.Request.ResourceType
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: LootBoxV3PurchaseV1.Request.ResourceType
        PURCHASE_NUM_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: LootBoxV3PurchaseV1.Request.ResourceType
        loot_box_product_id: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        purchase_num: int
        purchase_token: str
        resource_type: LootBoxV3PurchaseV1.Request.ResourceType
        transaction_id: str
        def __init__(self, loot_box_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., resource_type: _Optional[_Union[LootBoxV3PurchaseV1.Request.ResourceType, str]] = ..., purchase_token: _Optional[str] = ..., purchase_num: _Optional[int] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["extra_player_inventories", "loot_box_content_set_prizes", "pickup_extra_player_inventories", "player_inventories", "transaction_id", "wallet"]
        EXTRA_PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        LOOT_BOX_CONTENT_SET_PRIZES_FIELD_NUMBER: _ClassVar[int]
        PICKUP_EXTRA_PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        extra_player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        loot_box_content_set_prizes: _containers.RepeatedCompositeFieldContainer[_v3_pb2.LootBoxContentSetPrizes]
        pickup_extra_player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        transaction_id: str
        wallet: _v3_pb2_1.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., loot_box_content_set_prizes: _Optional[_Iterable[_Union[_v3_pb2.LootBoxContentSetPrizes, _Mapping]]] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., extra_player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., wallet: _Optional[_Union[_v3_pb2_1.Wallet, _Mapping]] = ..., pickup_extra_player_inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
