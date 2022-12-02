from takasho.schema.fes.resource.subscription.renewal_reward import v1_pb2 as _v1_pb2
from takasho.schema.common_featureset.resource.player_inventory import v1_pb2 as _v1_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RenewalRewardGetAvailableV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["renewal_rewards"]
        RENEWAL_REWARDS_FIELD_NUMBER: _ClassVar[int]
        renewal_rewards: _containers.RepeatedCompositeFieldContainer[_v1_pb2.RenewalReward]
        def __init__(self, renewal_rewards: _Optional[_Iterable[_Union[_v1_pb2.RenewalReward, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class RenewalRewardReceiveV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["inventories", "renewal_counts", "renewal_rewards"]
        INVENTORIES_FIELD_NUMBER: _ClassVar[int]
        RENEWAL_COUNTS_FIELD_NUMBER: _ClassVar[int]
        RENEWAL_REWARDS_FIELD_NUMBER: _ClassVar[int]
        inventories: _containers.RepeatedCompositeFieldContainer[_v1_pb2_1.PlayerInventory]
        renewal_counts: _containers.RepeatedCompositeFieldContainer[_v1_pb2.RenewalCount]
        renewal_rewards: _containers.RepeatedCompositeFieldContainer[_v1_pb2.RenewalReward]
        def __init__(self, renewal_rewards: _Optional[_Iterable[_Union[_v1_pb2.RenewalReward, _Mapping]]] = ..., inventories: _Optional[_Iterable[_Union[_v1_pb2_1.PlayerInventory, _Mapping]]] = ..., renewal_counts: _Optional[_Iterable[_Union[_v1_pb2.RenewalCount, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
