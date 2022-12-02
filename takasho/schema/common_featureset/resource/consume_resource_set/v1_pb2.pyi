from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NO_CONSUME: ResourceType
PLAYER_KEY_VALUE: ResourceType
VIRTUAL_CURRENCY: ResourceType

class ConsumeResource(_message.Message):
    __slots__ = ["consume_resource_id", "priority", "resource_key"]
    CONSUME_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_KEY_FIELD_NUMBER: _ClassVar[int]
    consume_resource_id: str
    priority: int
    resource_key: str
    def __init__(self, consume_resource_id: _Optional[str] = ..., resource_key: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class ConsumeResourceSet(_message.Message):
    __slots__ = ["amount", "consume_resource_set_id", "consume_resources", "resource_type"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CONSUME_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CONSUME_RESOURCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    amount: int
    consume_resource_set_id: str
    consume_resources: _containers.RepeatedCompositeFieldContainer[ConsumeResource]
    resource_type: ResourceType
    def __init__(self, consume_resource_set_id: _Optional[str] = ..., resource_type: _Optional[_Union[ResourceType, str]] = ..., amount: _Optional[int] = ..., consume_resources: _Optional[_Iterable[_Union[ConsumeResource, _Mapping]]] = ...) -> None: ...

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
