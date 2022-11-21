from takasho.schema.common_featureset.resource.system import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SystemAuthorizeV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["device_account", "device_info", "device_password"]
        DEVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
        DEVICE_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        device_account: str
        device_info: _v1_pb2.DeviceInfo
        device_password: str
        def __init__(self, device_account: _Optional[str] = ..., device_password: _Optional[str] = ..., device_info: _Optional[_Union[_v1_pb2.DeviceInfo, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_id", "session_token"]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        player_id: str
        session_token: str
        def __init__(self, session_token: _Optional[str] = ..., player_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class SystemAuthorizeV3(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["device_account", "device_info", "device_password", "id_token"]
        DEVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
        DEVICE_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
        device_account: str
        device_info: _v1_pb2.DeviceInfo
        device_password: str
        id_token: str
        def __init__(self, device_account: _Optional[str] = ..., device_password: _Optional[str] = ..., device_info: _Optional[_Union[_v1_pb2.DeviceInfo, _Mapping]] = ..., id_token: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_id", "session_token"]
        PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        player_id: str
        session_token: str
        def __init__(self, session_token: _Optional[str] = ..., player_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class SystemDeletePlayerStatusV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "player_status"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STATUS_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_status: _v1_pb2.PlayerStatus
        def __init__(self, player_status: _Optional[_Union[_v1_pb2.PlayerStatus, _Mapping]] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class SystemGetPlayerStatusV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_status", "total_login_days"]
        PLAYER_STATUS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGIN_DAYS_FIELD_NUMBER: _ClassVar[int]
        player_status: int
        total_login_days: int
        def __init__(self, player_status: _Optional[int] = ..., total_login_days: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class SystemGetPlayerStatusV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["ban_statuses", "player_statuses", "total_login_days"]
        BAN_STATUSES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STATUSES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGIN_DAYS_FIELD_NUMBER: _ClassVar[int]
        ban_statuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.BanStatus]
        player_statuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerStatus]
        total_login_days: int
        def __init__(self, player_statuses: _Optional[_Iterable[_Union[_v1_pb2.PlayerStatus, _Mapping]]] = ..., ban_statuses: _Optional[_Iterable[_Union[_v1_pb2.BanStatus, _Mapping]]] = ..., total_login_days: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class SystemGetWebTokenV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["id_token"]
        ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
        id_token: str
        def __init__(self, id_token: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class SystemRecordLoginHistoryV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["logged_in_at"]
        LOGGED_IN_AT_FIELD_NUMBER: _ClassVar[int]
        logged_in_at: int
        def __init__(self, logged_in_at: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class SystemSetPlayerStatusV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "player_status"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STATUS_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        player_status: _v1_pb2.PlayerStatus
        def __init__(self, player_status: _Optional[_Union[_v1_pb2.PlayerStatus, _Mapping]] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["ban_statuses", "player_statuses", "total_login_days"]
        BAN_STATUSES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_STATUSES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LOGIN_DAYS_FIELD_NUMBER: _ClassVar[int]
        ban_statuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.BanStatus]
        player_statuses: _containers.RepeatedCompositeFieldContainer[_v1_pb2.PlayerStatus]
        total_login_days: int
        def __init__(self, player_statuses: _Optional[_Iterable[_Union[_v1_pb2.PlayerStatus, _Mapping]]] = ..., ban_statuses: _Optional[_Iterable[_Union[_v1_pb2.BanStatus, _Mapping]]] = ..., total_login_days: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
