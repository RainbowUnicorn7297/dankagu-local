from takasho.schema.common_featureset.resource.baas_product import v1_pb2 as _v1_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaasProductGetAvailableByIDsV1(_message.Message):
    __slots__ = []
    class Request(_message.Message):
        __slots__ = ["product_ids"]
        PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
        product_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, product_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["baas_products"]
        BAAS_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        baas_products: _containers.RepeatedCompositeFieldContainer[_v1_pb2.BaasProduct]
        def __init__(self, baas_products: _Optional[_Iterable[_Union[_v1_pb2.BaasProduct, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
