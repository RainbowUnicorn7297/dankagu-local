from takasho.schema.common_featureset.resource.game_product import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.wallet import v3_pb2 as _v3_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1_1
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameProductGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion", "max_results", "page_token"]
        class Condition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Criterion(_message.Message):
            __slots__ = ["condition", "labels"]
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            LABELS_FIELD_NUMBER: _ClassVar[int]
            condition: GameProductGetAvailableV1.Request.Condition
            labels: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, labels: _Optional[_Iterable[str]] = ..., condition: _Optional[_Union[GameProductGetAvailableV1.Request.Condition, str]] = ...) -> None: ...
        AND: GameProductGetAvailableV1.Request.Condition
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        OR: GameProductGetAvailableV1.Request.Condition
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        criterion: GameProductGetAvailableV1.Request.Criterion
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ..., criterion: _Optional[_Union[GameProductGetAvailableV1.Request.Criterion, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["game_products", "next_page_token", "prev_page_token"]
        GAME_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        game_products: _containers.RepeatedCompositeFieldContainer[_v1_pb2.GameProduct]
        next_page_token: str
        prev_page_token: str
        def __init__(self, game_products: _Optional[_Iterable[_Union[_v1_pb2.GameProduct, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GameProductPurchaseAndSavePlayerStorageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "game_product_id", "next_revision", "previous_revision", "resource_type", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        GAME_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: GameProductPurchaseAndSavePlayerStorageV1.Request.ResourceType
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: GameProductPurchaseAndSavePlayerStorageV1.Request.ResourceType
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        game_product_id: str
        next_revision: str
        previous_revision: str
        resource_type: GameProductPurchaseAndSavePlayerStorageV1.Request.ResourceType
        transaction_id: str
        def __init__(self, game_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., resource_type: _Optional[_Union[GameProductPurchaseAndSavePlayerStorageV1.Request.ResourceType, str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "game_product", "player_inventory", "revision", "transaction_id", "wallet"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        GAME_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORY_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        game_product: _v1_pb2.GameProduct
        player_inventory: _v1_pb2_1.PlayerInventory
        revision: str
        transaction_id: str
        wallet: _v3_pb2.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., player_inventory: _Optional[_Union[_v1_pb2_1.PlayerInventory, _Mapping]] = ..., game_product: _Optional[_Union[_v1_pb2.GameProduct, _Mapping]] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GameProductPurchaseAndSavePlayerStorageV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "game_product_id", "next_revision", "player_event_logs", "previous_revision", "purchase_num", "resource_type", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        GAME_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: GameProductPurchaseAndSavePlayerStorageV2.Request.ResourceType
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_NUM_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: GameProductPurchaseAndSavePlayerStorageV2.Request.ResourceType
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        game_product_id: str
        next_revision: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerEventLog]
        previous_revision: str
        purchase_num: int
        resource_type: GameProductPurchaseAndSavePlayerStorageV2.Request.ResourceType
        transaction_id: str
        def __init__(self, game_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., resource_type: _Optional[_Union[GameProductPurchaseAndSavePlayerStorageV2.Request.ResourceType, str]] = ..., purchase_num: _Optional[int] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "game_product", "player_inventories", "revision", "transaction_id", "wallet"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        GAME_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        game_product: _v1_pb2.GameProduct
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerInventory]
        revision: str
        transaction_id: str
        wallet: _v3_pb2.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerInventory, _Mapping]]] = ..., game_product: _Optional[_Union[_v1_pb2.GameProduct, _Mapping]] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GameProductPurchaseV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["game_product_id", "resource_type", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        GAME_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: GameProductPurchaseV1.Request.ResourceType
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: GameProductPurchaseV1.Request.ResourceType
        game_product_id: str
        resource_type: GameProductPurchaseV1.Request.ResourceType
        transaction_id: str
        def __init__(self, game_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., resource_type: _Optional[_Union[GameProductPurchaseV1.Request.ResourceType, str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["game_product", "player_inventory", "transaction_id", "wallet"]
        GAME_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORY_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        game_product: _v1_pb2.GameProduct
        player_inventory: _v1_pb2_1.PlayerInventory
        transaction_id: str
        wallet: _v3_pb2.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., player_inventory: _Optional[_Union[_v1_pb2_1.PlayerInventory, _Mapping]] = ..., game_product: _Optional[_Union[_v1_pb2.GameProduct, _Mapping]] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class GameProductPurchaseV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["game_product_id", "player_event_logs", "purchase_num", "resource_type", "transaction_id"]
        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        GAME_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUE: GameProductPurchaseV2.Request.ResourceType
        PURCHASE_NUM_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY: GameProductPurchaseV2.Request.ResourceType
        game_product_id: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerEventLog]
        purchase_num: int
        resource_type: GameProductPurchaseV2.Request.ResourceType
        transaction_id: str
        def __init__(self, game_product_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., resource_type: _Optional[_Union[GameProductPurchaseV2.Request.ResourceType, str]] = ..., purchase_num: _Optional[int] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["game_product", "player_inventories", "transaction_id", "wallet"]
        GAME_PRODUCT_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        game_product: _v1_pb2.GameProduct
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerInventory]
        transaction_id: str
        wallet: _v3_pb2.Wallet
        def __init__(self, transaction_id: _Optional[str] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerInventory, _Mapping]]] = ..., game_product: _Optional[_Union[_v1_pb2.GameProduct, _Mapping]] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
