from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

APPLE: PlatformType
DESCRIPTOR: _descriptor.FileDescriptor
EDITOR: PlatformType
GOOGLE: PlatformType
LCX: BaasType
NPF: BaasType
UNKNOWN: PlatformType

class BanStatus(_message.Message):
    __slots__ = ["description", "expired_at", "has_expired_at", "status"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    description: str
    expired_at: int
    has_expired_at: bool
    status: int
    def __init__(self, status: _Optional[int] = ..., description: _Optional[str] = ..., expired_at: _Optional[int] = ..., has_expired_at: bool = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ["platform"]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    platform: PlatformType
    def __init__(self, platform: _Optional[_Union[PlatformType, str]] = ...) -> None: ...

class PlayerStatus(_message.Message):
    __slots__ = ["description", "expired_at", "has_expired_at", "status"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    description: str
    expired_at: int
    has_expired_at: bool
    status: int
    def __init__(self, status: _Optional[int] = ..., description: _Optional[str] = ..., expired_at: _Optional[int] = ..., has_expired_at: bool = ...) -> None: ...

class PlatformType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class BaasType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
