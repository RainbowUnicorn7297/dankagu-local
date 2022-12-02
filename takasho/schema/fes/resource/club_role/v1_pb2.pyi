from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

ASSIGN_SUBLEADER: ClubUpdateRoleType
DESCRIPTOR: _descriptor.FileDescriptor
LEADER: ClubRole
MEMBER: ClubRole
REPLACE_LEADER: ClubUpdateRoleType
SUB_LEADER: ClubRole
UNASSIGN_SUBLEADER: ClubUpdateRoleType
UNKNOWN_ROLE: ClubRole
UNKNOWN_UPDATE_TYPE: ClubUpdateRoleType

class ClubRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ClubUpdateRoleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
