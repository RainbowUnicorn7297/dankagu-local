from takasho.schema.common_featureset.resource.game_message import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameMessageGetMessageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["max_results", "page_token"]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["messages", "next_page_token", "prev_page_token"]
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[_v1_pb2.GameMessage]
        next_page_token: str
        prev_page_token: str
        def __init__(self, messages: _Optional[_Iterable[_Union[_v1_pb2.GameMessage, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GameMessageGetUnreadMessageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["max_results", "page_token"]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        max_results: int
        page_token: str
        def __init__(self, page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["messages", "next_page_token", "prev_page_token"]
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[_v1_pb2.GameMessage]
        next_page_token: str
        prev_page_token: str
        def __init__(self, messages: _Optional[_Iterable[_Union[_v1_pb2.GameMessage, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GameMessageReceiveMessageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["message_ids"]
        MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
        message_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, message_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
