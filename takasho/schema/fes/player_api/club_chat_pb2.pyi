from takasho.schema.fes.resource.club_chat import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClubChatCreateMessage(_message.Message):
    __slots__ = []
    class Message(_message.Message):
        __slots__ = ["club_id", "content", "message_id", "message_type"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        content: str
        message_id: str
        message_type: _v1_pb2.MessageType
        def __init__(self, club_id: _Optional[str] = ..., message_id: _Optional[str] = ..., message_type: _Optional[_Union[_v1_pb2.MessageType, str]] = ..., content: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ["messages"]
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[ClubChatCreateMessage.Message]
        def __init__(self, messages: _Optional[_Iterable[_Union[ClubChatCreateMessage.Message, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["message"]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ClubChatMessage]
        def __init__(self, message: _Optional[_Iterable[_Union[_v1_pb2.ClubChatMessage, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ClubChatGet(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["club_id", "max_results", "page_token", "player_storage_keys", "types"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STORAGE_KEYS_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        max_results: int
        page_token: str
        player_storage_keys: _containers.RepeatedScalarFieldContainer[str]
        types: _containers.RepeatedScalarFieldContainer[_v1_pb2.MessageType]
        def __init__(self, club_id: _Optional[str] = ..., types: _Optional[_Iterable[_Union[_v1_pb2.MessageType, str]]] = ..., player_storage_keys: _Optional[_Iterable[str]] = ..., max_results: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["message", "next_page_token", "prev_page_token"]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        message: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ClubChatMessage]
        next_page_token: str
        prev_page_token: str
        def __init__(self, message: _Optional[_Iterable[_Union[_v1_pb2.ClubChatMessage, _Mapping]]] = ..., prev_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class ClubChatGetMessagesCount(_message.Message):
    __slots__ = []
    class MessageCount(_message.Message):
        __slots__ = ["club_id", "messages_count"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        messages_count: int
        def __init__(self, club_id: _Optional[str] = ..., messages_count: _Optional[int] = ...) -> None: ...
    class MessageID(_message.Message):
        __slots__ = ["club_id", "message_id"]
        CLUB_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        club_id: str
        message_id: str
        def __init__(self, club_id: _Optional[str] = ..., message_id: _Optional[str] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ["ignore_message_types", "ignore_my_message", "message_ids"]
        IGNORE_MESSAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
        IGNORE_MY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
        ignore_message_types: _containers.RepeatedScalarFieldContainer[_v1_pb2.MessageType]
        ignore_my_message: bool
        message_ids: _containers.RepeatedCompositeFieldContainer[ClubChatGetMessagesCount.MessageID]
        def __init__(self, message_ids: _Optional[_Iterable[_Union[ClubChatGetMessagesCount.MessageID, _Mapping]]] = ..., ignore_message_types: _Optional[_Iterable[_Union[_v1_pb2.MessageType, str]]] = ..., ignore_my_message: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["message_counts"]
        MESSAGE_COUNTS_FIELD_NUMBER: _ClassVar[int]
        message_counts: _containers.RepeatedCompositeFieldContainer[ClubChatGetMessagesCount.MessageCount]
        def __init__(self, message_counts: _Optional[_Iterable[_Union[ClubChatGetMessagesCount.MessageCount, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
