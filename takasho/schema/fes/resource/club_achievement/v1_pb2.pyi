from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DATE_LINE: ResetType
DESCRIPTOR: _descriptor.FileDescriptor
NONE: ResetType
WEEK_LINE: ResetType

class ClubAchievement(_message.Message):
    __slots__ = ["category", "closed_at", "club_achievement_id", "date_line", "day_of_week", "opened_at", "points", "reset_type", "unlocked", "value"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    CLUB_ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_LINE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    OPENED_AT_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    RESET_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    category: str
    closed_at: int
    club_achievement_id: str
    date_line: str
    day_of_week: int
    opened_at: int
    points: int
    reset_type: ResetType
    unlocked: bool
    value: bytes
    def __init__(self, club_achievement_id: _Optional[str] = ..., value: _Optional[bytes] = ..., opened_at: _Optional[int] = ..., closed_at: _Optional[int] = ..., reset_type: _Optional[_Union[ResetType, str]] = ..., date_line: _Optional[str] = ..., day_of_week: _Optional[int] = ..., category: _Optional[str] = ..., points: _Optional[int] = ..., unlocked: bool = ...) -> None: ...

class Criteria(_message.Message):
    __slots__ = ["category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: str
    def __init__(self, category: _Optional[str] = ...) -> None: ...

class ResetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
