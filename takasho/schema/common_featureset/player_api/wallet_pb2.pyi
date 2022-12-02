from takasho.schema.common_featureset.resource.wallet import v3_pb2 as _v3_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WalletGetBalancesV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["balance"]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        balance: _containers.RepeatedCompositeFieldContainer[_v3_pb2.Wallet]
        def __init__(self, balance: _Optional[_Iterable[_Union[_v3_pb2.Wallet, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class WalletGetBalancesV2(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["expired_at"]
        EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
        expired_at: int
        def __init__(self, expired_at: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["expiration", "expired_at", "total"]
        EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        expiration: _v3_pb2.Wallet
        expired_at: int
        total: _v3_pb2.Wallet
        def __init__(self, total: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ..., expiration: _Optional[_Union[_v3_pb2.Wallet, _Mapping]] = ..., expired_at: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
