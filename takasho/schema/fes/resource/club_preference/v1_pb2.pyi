from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClubPreference(_message.Message):
    __slots__ = ["approval_policy", "character_id", "name", "play_style", "profile", "searchable"]
    class ApprovalPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class PlayStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    APPROVAL_POLICY_FIELD_NUMBER: _ClassVar[int]
    AUTO: ClubPreference.ApprovalPolicy
    BEGINNER: ClubPreference.PlayStyle
    CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
    GATTSURI: ClubPreference.PlayStyle
    MANUAL: ClubPreference.ApprovalPolicy
    MATTARI: ClubPreference.PlayStyle
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAY_STYLE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SEARCHABLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_POLICY: ClubPreference.ApprovalPolicy
    UNKNOWN_STYLE: ClubPreference.PlayStyle
    approval_policy: ClubPreference.ApprovalPolicy
    character_id: str
    name: str
    play_style: ClubPreference.PlayStyle
    profile: str
    searchable: bool
    def __init__(self, name: _Optional[str] = ..., profile: _Optional[str] = ..., play_style: _Optional[_Union[ClubPreference.PlayStyle, str]] = ..., approval_policy: _Optional[_Union[ClubPreference.ApprovalPolicy, str]] = ..., searchable: bool = ..., character_id: _Optional[str] = ...) -> None: ...
