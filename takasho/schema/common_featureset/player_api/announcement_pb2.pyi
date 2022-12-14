from takasho.schema.common_featureset.resource.announcement import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.extra_announcement import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnnouncementGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["language_code", "max_results", "page_token"]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        language_code: str
        max_results: int
        page_token: str
        def __init__(self, language_code: _Optional[str] = ..., page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["announcements", "base_image_url", "extra_announcements", "next_page_token", "prev_page_token"]
        ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
        BASE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        EXTRA_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        PREV_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        announcements: _containers.RepeatedCompositeFieldContainer[_v1_pb2.Announcement]
        base_image_url: str
        extra_announcements: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.ExtraAnnouncement]
        next_page_token: str
        prev_page_token: str
        def __init__(self, announcements: _Optional[_Iterable[_Union[_v1_pb2.Announcement, _Mapping]]] = ..., base_image_url: _Optional[str] = ..., next_page_token: _Optional[str] = ..., prev_page_token: _Optional[str] = ..., extra_announcements: _Optional[_Iterable[_Union[_v1_pb2_1.ExtraAnnouncement, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class AnnouncementGetCredentialV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["credential", "url"]
        CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        credential: str
        url: str
        def __init__(self, credential: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
