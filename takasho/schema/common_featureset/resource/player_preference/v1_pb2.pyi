from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

ALLOW_ALL: AllowFriendRequestType
DESCRIPTOR: _descriptor.FileDescriptor
FORBID_ALL: AllowFriendRequestType
NO_PREFERENCE: AllowFriendRequestType

class PlayerPreference(_message.Message):
    __slots__ = ["allow_friend_request", "birth_month", "birth_year", "consented_privacy_policy_version", "consented_tos_version", "country", "created_at", "language", "max_friend_number", "max_friend_request_queue_length", "nickname", "nickname_updated_at", "opt_out", "updated_at"]
    ALLOW_FRIEND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BIRTH_MONTH_FIELD_NUMBER: _ClassVar[int]
    BIRTH_YEAR_FIELD_NUMBER: _ClassVar[int]
    CONSENTED_PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONSENTED_TOS_VERSION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_FRIEND_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MAX_FRIEND_REQUEST_QUEUE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    OPT_OUT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    allow_friend_request: AllowFriendRequestType
    birth_month: int
    birth_year: int
    consented_privacy_policy_version: str
    consented_tos_version: str
    country: str
    created_at: int
    language: str
    max_friend_number: int
    max_friend_request_queue_length: int
    nickname: str
    nickname_updated_at: int
    opt_out: bool
    updated_at: int
    def __init__(self, birth_year: _Optional[int] = ..., birth_month: _Optional[int] = ..., country: _Optional[str] = ..., language: _Optional[str] = ..., opt_out: bool = ..., consented_tos_version: _Optional[str] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., nickname: _Optional[str] = ..., consented_privacy_policy_version: _Optional[str] = ..., nickname_updated_at: _Optional[int] = ..., allow_friend_request: _Optional[_Union[AllowFriendRequestType, str]] = ..., max_friend_number: _Optional[int] = ..., max_friend_request_queue_length: _Optional[int] = ...) -> None: ...

class AllowFriendRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
