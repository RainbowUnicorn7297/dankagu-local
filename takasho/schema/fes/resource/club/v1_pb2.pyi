from takasho.schema.fes.resource.club_preference import v1_pb2 as _v1_pb2
from takasho.schema.fes.resource.club_storage import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Club(_message.Message):
    __slots__ = ["club_id", "club_storage_entries", "organized_at", "preference"]
    CLUB_ID_FIELD_NUMBER: _ClassVar[int]
    CLUB_STORAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ORGANIZED_AT_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    club_id: str
    club_storage_entries: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.ClubStorageEntry]
    organized_at: int
    preference: _v1_pb2.ClubPreference
    def __init__(self, club_id: _Optional[str] = ..., organized_at: _Optional[int] = ..., preference: _Optional[_Union[_v1_pb2.ClubPreference, _Mapping]] = ..., club_storage_entries: _Optional[_Iterable[_Union[_v1_pb2_1.ClubStorageEntry, _Mapping]]] = ...) -> None: ...
