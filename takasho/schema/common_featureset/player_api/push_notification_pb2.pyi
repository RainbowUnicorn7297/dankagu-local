from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PushNotificationGetConfigV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["receivable"]
        RECEIVABLE_FIELD_NUMBER: _ClassVar[int]
        receivable: bool
        def __init__(self, receivable: bool = ...) -> None: ...
    def __init__(self) -> None: ...

class PushNotificationGetConfigV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["topic_ids"]
        TOPIC_IDS_FIELD_NUMBER: _ClassVar[int]
        topic_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, topic_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PushNotificationSetConfigV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["receivable"]
        RECEIVABLE_FIELD_NUMBER: _ClassVar[int]
        receivable: bool
        def __init__(self, receivable: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["receivable"]
        RECEIVABLE_FIELD_NUMBER: _ClassVar[int]
        receivable: bool
        def __init__(self, receivable: bool = ...) -> None: ...
    def __init__(self) -> None: ...

class PushNotificationSetConfigV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["topic_ids"]
        TOPIC_IDS_FIELD_NUMBER: _ClassVar[int]
        topic_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, topic_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
