from takasho.schema.common_featureset.resource.player_preference import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_event_log import v1_pb2 as _v1_pb2_1
from takasho.schema.common_featureset.resource.player_storage import v2_pb2 as _v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerPreferenceGetMonthlyBillingLimitV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["exits_monthly_billing_limit", "max_age", "min_age", "monthly_billing_limit"]
        EXITS_MONTHLY_BILLING_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MAX_AGE_FIELD_NUMBER: _ClassVar[int]
        MIN_AGE_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_BILLING_LIMIT_FIELD_NUMBER: _ClassVar[int]
        exits_monthly_billing_limit: bool
        max_age: int
        min_age: int
        monthly_billing_limit: int
        def __init__(self, min_age: _Optional[int] = ..., max_age: _Optional[int] = ..., monthly_billing_limit: _Optional[int] = ..., exits_monthly_billing_limit: bool = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerPreferenceGetMonthlyPurchaseSummaryV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["monthly_billing_limit", "paid_amount"]
        MONTHLY_BILLING_LIMIT_FIELD_NUMBER: _ClassVar[int]
        PAID_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        monthly_billing_limit: int
        paid_amount: int
        def __init__(self, monthly_billing_limit: _Optional[int] = ..., paid_amount: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerPreferenceGetPreferenceV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_short_id", "preference"]
        PLAYER_SHORT_ID_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        player_short_id: str
        preference: _v1_pb2.PlayerPreference
        def __init__(self, preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., player_short_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerPreferenceSetPreferenceAndSavePlayerStorageV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["entries", "next_revision", "preference", "previous_revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        NEXT_REVISION_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        next_revision: str
        preference: _v1_pb2.PlayerPreference
        previous_revision: str
        def __init__(self, preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., next_revision: _Optional[str] = ..., previous_revision: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["entries", "player_short_id", "preference", "revision"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SHORT_ID_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_v2_pb2.Entry]
        player_short_id: str
        preference: _v1_pb2.PlayerPreference
        revision: str
        def __init__(self, preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., player_short_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[_v2_pb2.Entry, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlayerPreferenceSetPreferenceV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["player_event_logs", "preference"]
        PLAYER_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        player_event_logs: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerEventLog]
        preference: _v1_pb2.PlayerPreference
        def __init__(self, preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., player_event_logs: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerEventLog, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["player_short_id", "preference"]
        PLAYER_SHORT_ID_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        player_short_id: str
        preference: _v1_pb2.PlayerPreference
        def __init__(self, preference: _Optional[_Union[_v1_pb2.PlayerPreference, _Mapping]] = ..., player_short_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
