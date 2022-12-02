from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Wallet(_message.Message):
    __slots__ = ["player_key_values", "virtual_currencies"]
    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class PlayerKeyValue(_message.Message):
        __slots__ = ["amount", "key"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        amount: int
        key: str
        def __init__(self, key: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...
    class VirtualCurrency(_message.Message):
        __slots__ = ["amount", "platform", "virtual_currency_name"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
        amount: int
        platform: Wallet.Platform
        virtual_currency_name: str
        def __init__(self, virtual_currency_name: _Optional[str] = ..., platform: _Optional[_Union[Wallet.Platform, str]] = ..., amount: _Optional[int] = ...) -> None: ...
    APPLE: Wallet.Platform
    GOOGLE: Wallet.Platform
    NONE: Wallet.Platform
    PLAYER_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    player_key_values: _containers.RepeatedCompositeFieldContainer[Wallet.PlayerKeyValue]
    virtual_currencies: _containers.RepeatedCompositeFieldContainer[Wallet.VirtualCurrency]
    def __init__(self, virtual_currencies: _Optional[_Iterable[_Union[Wallet.VirtualCurrency, _Mapping]]] = ..., player_key_values: _Optional[_Iterable[_Union[Wallet.PlayerKeyValue, _Mapping]]] = ...) -> None: ...
