from takasho.schema.fes.resource.login_bonus import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.login_bonus import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1_1
from takasho.schema.fes.resource.comeback_login_bonus import v1_pb2 as _v1_pb2_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginBonusCountUpProgressV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["bingo_login_bonuses", "campaign_login_bonuses", "comeback_login_bonus", "comeback_login_bonus_progresses", "player_inventories"]
        BINGO_LOGIN_BONUSES_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_LOGIN_BONUSES_FIELD_NUMBER: _ClassVar[int]
        COMEBACK_LOGIN_BONUS_FIELD_NUMBER: _ClassVar[int]
        COMEBACK_LOGIN_BONUS_PROGRESSES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        bingo_login_bonuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.BingoLoginBonus]
        campaign_login_bonuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.LoginBonus]
        comeback_login_bonus: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1_1.ComebackLoginBonus]
        comeback_login_bonus_progresses: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1_1.ComebackLoginBonusProgress]
        player_inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1.PlayerInventory]
        def __init__(self, bingo_login_bonuses: _Optional[_Iterable[_Union[_v1_pb2.BingoLoginBonus, _Mapping]]] = ..., campaign_login_bonuses: _Optional[_Iterable[_Union[_v1_pb2_1.LoginBonus, _Mapping]]] = ..., player_inventories: _Optional[_Iterable[_Union[_v1_pb2_1_1.PlayerInventory, _Mapping]]] = ..., comeback_login_bonus: _Optional[_Iterable[_Union[_v1_pb2_1_1_1.ComebackLoginBonus, _Mapping]]] = ..., comeback_login_bonus_progresses: _Optional[_Iterable[_Union[_v1_pb2_1_1_1.ComebackLoginBonusProgress, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LoginBonusGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["bingo_login_bonuses", "comeback_login_bonus", "comeback_login_bonus_progresses"]
        BINGO_LOGIN_BONUSES_FIELD_NUMBER: _ClassVar[int]
        COMEBACK_LOGIN_BONUS_FIELD_NUMBER: _ClassVar[int]
        COMEBACK_LOGIN_BONUS_PROGRESSES_FIELD_NUMBER: _ClassVar[int]
        bingo_login_bonuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.BingoLoginBonus]
        comeback_login_bonus: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1_1.ComebackLoginBonus]
        comeback_login_bonus_progresses: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1_1_1.ComebackLoginBonusProgress]
        def __init__(self, bingo_login_bonuses: _Optional[_Iterable[_Union[_v1_pb2.BingoLoginBonus, _Mapping]]] = ..., comeback_login_bonus: _Optional[_Iterable[_Union[_v1_pb2_1_1_1.ComebackLoginBonus, _Mapping]]] = ..., comeback_login_bonus_progresses: _Optional[_Iterable[_Union[_v1_pb2_1_1_1.ComebackLoginBonusProgress, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
