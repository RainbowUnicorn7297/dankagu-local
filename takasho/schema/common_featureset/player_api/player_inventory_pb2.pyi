from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.wallet import v3_pb2 as _v3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerInventoryGetInventoriesAndCountV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion"]
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        criterion: _v1_pb2.Criterion
        def __init__(self, criterion: _Optional[_Union[_v1_pb2.Criterion, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["inventories", "inventories_count", "next_page_token", "prev_page_token"]
        INVENTORIES_COUNT_FIELD_NUMBER: _ClassVar[int]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        inventories_count: int
        next_page_token: str
        prev_page_token: str
        def __init__(self, inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., inventories_count: _Optional[int] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerInventoryGetInventoriesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion"]
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        criterion: _v1_pb2.Criterion
        def __init__(self, criterion: _Optional[_Union[_v1_pb2.Criterion, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["inventories", "next_page_token", "prev_page_token"]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerInventory]
        next_page_token: str
        prev_page_token: str
        def __init__(self, inventories: _Optional[_Iterable[_Union[_v1_pb2.PlayerInventory, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerInventoryGetReceivedInventoriesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["count", "page_token", "search_labels"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SEARCH_LABELS_FIELD_NUMBER: _ClassVar[int]
        count: int
        page_token: str
        search_labels: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, count: _Optional[int] = ..., search_labels: _Optional[_Iterable[str]] = ..., page_token: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["next_page_token", "prev_page_token", "received_inventories"]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        RECEIVED_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        next_page_token: str
        prev_page_token: str
        received_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ReceivedPlayerInventory]
        def __init__(self, received_inventories: _Optional[_Iterable[_Union[_v1_pb2.ReceivedPlayerInventory, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerInventoryReceiveV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["delete_inventory_ids", "entries", "next_revision", "player_event_logs", "previous_revision"]
        DELETE_INVENTORY_IDS_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        delete_inventory_ids: _containers.RepeatedScalarFieldContainer[str]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        previous_revision: str
        def __init__(self, delete_inventory_ids: _Optional[_Iterable[str]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "player_key_values", "revision", "wallet"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        WALLET_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        player_key_values: _containers.RepeatedCompositeFieldContainer[_v3_pb2.Wallet.PlayerKeyValue]
        revision: str
        wallet: _v3_pb2.Wallet
        def __init__(self, entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ..., wallet: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ..., player_key_values: _Optional[_Iterable[_Union[_v3_pb2.Wallet.PlayerKeyValue, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
