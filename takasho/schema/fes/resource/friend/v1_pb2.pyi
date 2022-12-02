from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Criterion(_message.Message):
    __slots__ = ["filter", "order_direction", "order_field"]
    class OrderDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class OrderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["club", "follow"]
        class Club(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Follow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ALL_CLUB: Criterion.Filter.Club
        ALL_FOLLOW: Criterion.Filter.Follow
        CLUB_FIELD_NUMBER: _ClassVar[int]
        FOLLOW_FIELD_NUMBER: _ClassVar[int]
        MUTUAL: Criterion.Filter.Follow
        NOT_MUTUAL: Criterion.Filter.Follow
        NOT_SAME_CLUB: Criterion.Filter.Club
        SAME_CLUB: Criterion.Filter.Club
        club: Criterion.Filter.Club
        follow: Criterion.Filter.Follow
        def __init__(self, follow: _Optional[_Union[Criterion.Filter.Follow, str]] = ..., club: _Optional[_Union[Criterion.Filter.Club, str]] = ...) -> None: ...
    ASC: Criterion.OrderDirection
    DESC: Criterion.OrderDirection
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGGED_IN_AT: Criterion.OrderField
    ORDER_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LEVEL: Criterion.OrderField
    UNKNOWN_ORDER_FIELD: Criterion.OrderField
    filter: Criterion.Filter
    order_direction: Criterion.OrderDirection
    order_field: Criterion.OrderField
    def __init__(self, order_field: _Optional[_Union[Criterion.OrderField, str]] = ..., order_direction: _Optional[_Union[Criterion.OrderDirection, str]] = ..., filter: _Optional[_Union[Criterion.Filter, _Mapping]] = ...) -> None: ...

class FollowStatus(_message.Message):
    __slots__ = ["is_followed", "is_following", "player_id"]
    IS_FOLLOWED_FIELD_NUMBER: _ClassVar[int]
    IS_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    is_followed: bool
    is_following: bool
    player_id: str
    def __init__(self, player_id: _Optional[str] = ..., is_following: bool = ..., is_followed: bool = ...) -> None: ...

class FriendPlayer(_message.Message):
    __slots__ = ["club_names", "is_followed", "is_following", "last_logged_in_at", "nickname", "player_id", "player_storage_entries"]
    CLUB_NAMES_FIELD_NUMBER: _ClassVar[int]
    IS_FOLLOWED_FIELD_NUMBER: _ClassVar[int]
    IS_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGGED_IN_AT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STORAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    club_names: _containers.RepeatedScalarFieldContainer[str]
    is_followed: bool
    is_following: bool
    last_logged_in_at: int
    nickname: str
    player_id: str
    player_storage_entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
    def __init__(self, player_id: _Optional[str] = ..., player_storage_entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., nickname: _Optional[str] = ..., club_names: _Optional[_Iterable[str]] = ..., is_following: bool = ..., is_followed: bool = ..., last_logged_in_at: _Optional[int] = ...) -> None: ...
