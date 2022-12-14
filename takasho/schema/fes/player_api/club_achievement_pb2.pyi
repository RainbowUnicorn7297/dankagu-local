from takasho.schema.fes.resource.club_achievement import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClubAchievementGetAvailable(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criteria", "max_results", "page_token"]
        CRITERIA_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        criteria: _v1_pb2.Criteria
        max_results: int
        page_token: str
        def __init__(self, criteria: _Optional[_Union[_v1_pb2.Criteria, _Mapping]] = ..., page_token: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["achievements", "next_page_token"]
        ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        achievements: _containers.RepeatedCompositeFieldContainer[_v1_pb2.ClubAchievement]
        next_page_token: str
        def __init__(self, achievements: _Optional[_Iterable[_Union[_v1_pb2.ClubAchievement, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class ClubAchievementUnlockAndIncrementClubScalar(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["achievement_id", "scalar_key"]
        ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        SCALAR_KEY_FIELD_NUMBER: _ClassVar[int]
        achievement_id: str
        scalar_key: str
        def __init__(self, achievement_id: _Optional[str] = ..., scalar_key: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
