from takasho.schema.common_featureset.resource.achievement import v1_pb2 as _v1_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerAchievement(_message.Message):
    __slots__ = ["achievement", "last_unlocked_at"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    LAST_UNLOCKED_AT_FIELD_NUMBER: _ClassVar[int]
    achievement: _v1_pb2.Achievement
    last_unlocked_at: int
    def __init__(self, achievement: _Optional[_Union[_v1_pb2.Achievement, _Mapping]] = ..., last_unlocked_at: _Optional[int] = ...) -> None: ...
