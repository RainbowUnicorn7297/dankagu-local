from takasho.schema.common_featureset.resource.achievement import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_achievement import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1_1
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerAchievementGetAvailableByIDsV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["achievement_ids"]
        ACHIEVEMENT_IDS_FIELD_NUMBER: _ClassVar[int]
        achievement_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, achievement_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_achievements"]
        PLAYER_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        player_achievements: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerAchievement]
        def __init__(self, player_achievements: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerAchievement, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerAchievementGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["criterion"]
        CRITERION_FIELD_NUMBER: _ClassVar[int]
        criterion: _v1_pb2.Criterion
        def __init__(self, criterion: _Optional[_Union[_v1_pb2.Criterion, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_achievements"]
        PLAYER_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        player_achievements: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerAchievement]
        def __init__(self, player_achievements: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerAchievement, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerAchievementUnlockAndSavePlayerStorageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["achievement_ids", "entries", "next_revision", "previous_revision"]
        ACHIEVEMENT_IDS_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        achievement_ids: _containers.RepeatedScalarFieldContainer[str]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        previous_revision: str
        def __init__(self, achievement_ids: _Optional[_Iterable[str]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "inventories", "player_achievements", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        player_achievements: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerAchievement]
        revision: str
        def __init__(self, player_achievements: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerAchievement, _Mapping]]] = ..., inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerAchievementUnlockV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["achievement_ids"]
        ACHIEVEMENT_IDS_FIELD_NUMBER: _ClassVar[int]
        achievement_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, achievement_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["inventories", "player_achievements"]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        player_achievements: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerAchievement]
        def __init__(self, player_achievements: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerAchievement, _Mapping]]] = ..., inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
