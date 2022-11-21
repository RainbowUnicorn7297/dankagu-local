from concurrent import futures
import logging
from typing import Any, Callable

import grpc
#from grpc_interceptor import ServerInterceptor
#from grpc_interceptor.exceptions import GrpcException

#from takasho.schema.common_featureset.player_api import ondemand_master_pb2
#from takasho.schema.common_featureset.player_api import ondemand_master_pb2_grpc
from takasho.schema.common_featureset.player_api import ondemand_master


# class ExceptionToStatusInterceptor(ServerInterceptor):

#     def intercept(
#         self,
#         method: Callable,
#         request: Any,
#         context: grpc.ServicerContext,
#         method_name: str,
#     ) -> Any:
#         """Override this method to implement a custom interceptor.

#          You should call method(request, context) to invoke the
#          next handler (either the RPC method implementation, or the
#          next interceptor in the list).

#          Args:
#              method: The next interceptor, or method implementation.
#              request: The RPC request, as a protobuf message.
#              context: The ServicerContext pass by gRPC to the service.
#              method_name: A string of the form
#                  "/protobuf.package.Service/Method"

#          Returns:
#              This should generally return the result of
#              method(request, context), which is typically the RPC
#              method response, as a protobuf message. The interceptor
#              is free to modify this in some way, however.
#          """
#         print('in interceptor')
#         try:
#             #reponse = method(bytes.fromhex('000000003E0A0F4F444D47656E657269635F426F6F740A154F444D47656E657269635F536563757265486173680A144F444D47656E657269635F5369676E6174757265')[5:], context)
#             return bytes.fromhex('0000000be8ba448034aad054336bf518d3dc1d30616b7de10d4168d58262cfe5b53599bb3259ad6a146fc3cd935ca1d655ec6d69e6ca4b974b4237385361b34d359065a8ce894d8377ea8d0d732433438d0b5fd776b9f84afc9c2c1950374214591e8061a61c9b312bfc7f29bec39e864640454b90920afd268ab2582fa979552f5ca3acbee5f0c5170fafc4f3c0a0768d07ddc91bd0606589ee8f584b0eb7316170bef6477356f4fc8bca639f0b76b59b85163bbb5de923e308ed49832c8e55c28ffea248cc738e98de6aa32b8a235416708797aafc5b7545cfd340758acad09bc828021e39c2da8fba13fc68777edab1d83d5fb451208de825f509ed9af685c85c4c2206e7e1b33f596a2a1ba08b11d4612db436299a181def0b2b33d64d55cbde31ebcb121823c8ef25247567302f2f5dd1cd25bc5a1eb2fa1997a131fd8e53e58a1eb87f065f47afb6a5e7c69002990143997b462903b9c483ac3c98ea59e5a789bba2cb2e5a76bf67a828d3b3f71e5b40331a30baac17327be423fb8128e174e300855aea67d50f4c87195e8c4b211f40ad5ee5454b4bda64a0e7081a1487e23cd4440a04c6be6543328c6fa5ec607272e6b1e2a5600143693237af3c2d0a23a1bd4b013208bb20f63b6bf317ac056e38065ce463f532ef58b6013ce954cfd9e6d67d561154fc76d1f6f130286e54565b7100f7c30d975cc60833bf75d6c591c74f46e2d5daa3b070226f9c34ac7e2e1216a35996738c829b011b91529a4bad9e90e11caf9d9ff4f499508e4dc07387151ff70191dbb274faca96d9512823a1672bb4cce52943e7020893726dca81032b216f1ce0404779f29b40259eec812f053da8f0eff2d1fed91b952fe99421f185a260776049f4851b965a4bd9cba63f1e6c66ce9433eb88b0d6524631a1964c1bd65365a952597a58ff5d8bebdf092a4f9e7c946b3c92aca0fc09e1ef1d6b10b06af3ac38692ffcc13ef89beefbb01137f8d3308659a53623dd573220d382c6b41ceb363686572c9e760cec45606c4bc4bb8e49ae6be08a73448291dce0df1675fe61bcbd040d917f7c40c231a9e6fe2aa1266996e32cae24d5c9ec98e40aeaf752b31884a180d9676cea50800f91714cc5011f3433cf2888a924cb714f20a59b9a1a80ce4bcb84565e3ebed3670570bde3ecd1176f6bc2b070aaf79e861d5789c1eb8348be3f73d2996571123bd6c20147776f9c36910bcb8d3cc4165016a829f5a8b6fa740e3390808afadcd718a8987020defc5b5fe1c2cd2f674ff01426d3602e76df386e72ec2552c116ee203a6c687d31ff4d6aec8ab372e9deb1b5702b49bf20638ff08c2667bf3773ce9695a4be8abf62389b131d1386e4511f11425c794f4d2ae076ce193464aaaf8b29ff3f1e5ca22f285f3c4781eeddeff6acea6befe4e792b8a087117d258619d16b56d3983f17508205647846d41455402aa884539512d9ae1781a34a430197ff80bf4750a457aaf22b4451154a8a31ba5cd634512c33bd37eea3b644b99c4e2dd31f3c613867f9555e517c7f1930544e9ba6dc08fdbc1037d15b2f718d5fc6edd5b445d7e176e7c5583d7be23fcef056a6190105efb24227b3f98d321a9fe74af005a5640448503dfbeafc93ec70c0920cdce14d10a13364228db44c8ca14dfd834c9d1a1920b596911632ffa0c60da0bb35368fbb6483f9304843994d277f1a2d11cc15d4d6b04f52271c6edbbd1dc730a934259c548e09bfe73c14f68df4e6fd8d13d35d571d5a85f6a3fa265faa251ca2961311eb24b31272d16fa31a612d8c30abec9a6ee4e883688be3c89ceecbc662372a75d1fd63c198cb177bc5decf7bcacb7df46c2a1443148fadba14f8b6242f85f6dc15b6b9cd40d9f2181c30e1d4086656d8d0ec78727777442e985c1007facf1390821abf7c8da2675d40219a520b9e852e40ec20128961421cd2c01fad075c4a2f08918ed5e082e6c136ffa73a1f09ff19371f4ed34eb8f248000dd1a6d8eeddaecd65bc7d8d1012f66abcd13c9c2ab8e59483d0a040de311482bdd7318c15504409c6142be63ad425c7356450d2cff4b472d0c98a0a0e18f553c48620b68b803c406983df1c4465ec9b2156f411dbfcfecf879343fc747be09dc41c4e0689807c00b35deb3bb59d1ba80562eb55e9b850dbf5f4a451ee57e24ccd2bc2ed48214594269969587c371d041285a0d4a314b4b943b5eb1dadc0d510b17cee31d23bfffcef6b861fcbbc34c828a53f1083be2a639f3144262d26c349ae735aede7e54427e8afd5179c9160929fd20f434b6ac7443e26884405aab11f621c93d16c33ccc9d11b10d091f629b4c8d2f4ae1c32153f2b3d56d4c754fe746878d1f628b7f02e806c8a36497657bd5486c165feb92bc5ea9fdd90ac4e1299d40907acc88410806ae61b56a5174681bea18cae6f15d3283c76158348e7d434a650f1f731bb79baf731dc8ada3fdfe1a98462bc9949f81f133eb7a0a7092edd09b9f9d36a8659088b3f699c6b20c2345a265b5ea247d7338f7a0ed9c55ead9c642f66b66d294b472a2c1b655b86f830dadb15be93abfdde62fbbb2d8dd54b897f9cd3eed862c24a5f089200f6763d7317098e1442138ca33ccd8565ed810f2661cdc24dbca39559dc1186a99aae632baedaeef5531a3cfab47c02e918446e0e67a92625e6778444471377c164edee1abfcca13a8b56478c06f36b55036418c430e27a0ae8a7f1fc1888fe459b6c60835b5e40c3e555448013b45d72cd3aa09de41907266b7be25979dcb7b6f88beb07fe9f3d4fb9745e793382492462ae3ed293963c208fdcb3e5adf44e3becb4dea5d059537fb4455dfd1d7016738a4c217636e3355c44c98c7ff922dcbefe8cae43b26cac677b35cab85f016599890fadf14586cdc430753fe4ae72e5186f39f1e140f88066b637513a5e2cd83bfc86a21c927f291f3b6a7f9ce2c306a94874a14e1b16bbdd280f7662a5be9cefbe999e60fcac2ba99100343daaeec3d53d8e23c11496074aeeb234156e44759d8c745e9b741b8b86c0039b842e76af7dd53b7f1db109246bb1ecfd204d7406bde4e1bcd1e21a74dd5b4744c81b4d038333af1101f4e99f9b08a6b2652d252f9253291b5d4e669121be91f1d2ea2e07a9a4b530eb28049a9b40d66d728a8848a18a9ac283caaa0c910ed9e0aa2284c53d106ad57d7df583e42c97a8984a31cfd58bf79dd582c66ce8644619033594b9f7e59b547bf2fe16ae7ff3665ac75c4e3b59c49dfdf1c7467dad1bf796087c524aac11a2c06085c39418ed8e5f6f2436822e7669960b62ffa29109f2d80c11f934276decb06ae5e71d61ff600b0fb7e73ebcf16bf3b45cd351d07b0154a77e723190f1ff4c49908fc08d82eb74589c566d9b0d1b288beb19bd269282cec38a584cddd059aa421985807c5228e7fd6dd91360e5e29f7f8d54c8d60890170e91e427def56366cbc139caa02b908e4e49bf86f10a308ead85c959254f08905ce0ace85348bcd24deac92579dfe776b0dfc884f92e858cde9504356daca374b5e519304e329993d13c005eddc9cfe9e29e0324b853bd5068ca1e946920126887a6318593d5d9e58748438fd9d0820b661bda4bb7d4a645fe56ccb329a4ea2d073ea9f35e790f45b66004d6090b056deef17b6b551113d356883215301f4658ceb509bc2640cd978282825b2b34d6126e40971b2630cf3adfc1b313ca52d2536891215bc655f8f5d67e2b4c8acc103c863f4000ea107efe44c95672093cd48bf6918c410f018fa1cccf212220b66446198f4202f338d657e1cbb63c65a86606e224992c34dafd51bb0a6370da40be6c5388a468a5a14eda405bdf8a1569ad79c7f6cf8333ebbf9989b467c8c530ed257894d4fd6aa012ee37929ed1e51ab9aab9bc3aaa170653da96bd80d2c5f08d275320bcd6b7f4434c7bb733bc7519f9a4a366bf83e3346eaa660f76005135806834637178e03e1d8a317f8738b67867db78caff5fff0b42d223a45aa4c02d85cf539fa9db3001fa1036f35cb33139ed1974d7bd517234598c74814599e1d492f00eac7aaf6eaca8a564863c099b5c5a4049e8c6dd78c41cdff99416e2672fe414b9ecd021e7347a06c6f3ed607e4a64650d42f8ef215dd9bc2cb0dbb23681e3a3ebee842401cbc2a6dba1d15b072ee573cd876e96158ce1d15fff28afc4db0c1de9b2ba428d367db58b883515f7fa836b55dd1537f63742007ef10cb20d8d806ba087c1789651aabca59a455f43778565509b4e59d38076d0918f526c06ae7ea6ec591ee746cd1a')[5:]
#         except GrpcException as e:
#             context.set_code(e.status_code)
#             context.set_details(e.details)
#             raise


def deserialize(request: bytes):
    return ondemand_master_pb2.OndemandMasterGetEntriesV2.Request.FromString(bytes.fromhex('000000003E0A0F4F444D47656E657269635F426F6F740A154F444D47656E657269635F536563757265486173680A144F444D47656E657269635F5369676E6174757265')[5:])


def serialize(response: Any):
    #b = ondemand_master_pb2.OndemandMasterGetEntriesV2.Response.SerializeToString(response)
    return response


def serve():
    port = '50051'
    #interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        #interceptors=interceptors
    )
    ondemand_master.add_OndemandMasterServicer_to_server(
        ondemand_master.OndemandMaster(), server)
    # rpc_method_handlers = {
    #         'GetEntriesV1': grpc.unary_unary_rpc_method_handler(
    #                 OndemandMaster.GetEntriesV1,
    #                 request_deserializer=deserialize,
    #                 #request_deserializer=lambda request: FromString(decrypt(request))
    #                 response_serializer=serialize,
    #         ),
    # }
    # generic_handler = grpc.method_handlers_generic_handler(
    #         'takasho.schema.common_featureset.player_api.OndemandMaster', rpc_method_handlers)
    # server.add_generic_rpc_handlers((generic_handler,))
    with open('keys/grpc.key', 'rb') as f:
        private_key = f.read()
    with open('keys/grpc.crt', 'rb') as f:
        certificate_chain = f.read()
    credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)])
    server.add_secure_port('[::]:' + port, credentials)
    server.start()
    print('Server started, listening on ' + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
