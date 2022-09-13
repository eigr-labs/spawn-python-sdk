# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/eigr/functions/protocol/actors/protocol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eigr.functions.protocol.actors import actor_pb2 as eigr_dot_functions_dot_protocol_dot_actors_dot_actor__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6protobuf/eigr/functions/protocol/actors/protocol.proto\x12\x17\x65igr.functions.protocol\x1a*eigr/functions/protocol/actors/actor.proto\x1a\x19google/protobuf/any.proto\"\x94\x01\n\x13RegistrationRequest\x12:\n\x0cservice_info\x18\x01 \x01(\x0b\x32$.eigr.functions.protocol.ServiceInfo\x12\x41\n\x0c\x61\x63tor_system\x18\x02 \x01(\x0b\x32+.eigr.functions.protocol.actors.ActorSystem\"\xd4\x01\n\x0bServiceInfo\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x17\n\x0fservice_version\x18\x02 \x01(\t\x12\x17\n\x0fservice_runtime\x18\x03 \x01(\t\x12\x1c\n\x14support_library_name\x18\x04 \x01(\t\x12\x1f\n\x17support_library_version\x18\x05 \x01(\t\x12\x1e\n\x16protocol_major_version\x18\x06 \x01(\x05\x12\x1e\n\x16protocol_minor_version\x18\x07 \x01(\x05\"v\n\tProxyInfo\x12\x1e\n\x16protocol_major_version\x18\x01 \x01(\x05\x12\x1e\n\x16protocol_minor_version\x18\x02 \x01(\x05\x12\x12\n\nproxy_name\x18\x03 \x01(\t\x12\x15\n\rproxy_version\x18\x04 \x01(\t\"\x86\x01\n\x14RegistrationResponse\x12\x36\n\x06status\x18\x01 \x01(\x0b\x32&.eigr.functions.protocol.RequestStatus\x12\x36\n\nproxy_info\x18\x02 \x01(\x0b\x32\".eigr.functions.protocol.ProxyInfo\".\n\x07\x43ontext\x12#\n\x05state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"\xd0\x01\n\x11InvocationRequest\x12;\n\x06system\x18\x01 \x01(\x0b\x32+.eigr.functions.protocol.actors.ActorSystem\x12\x34\n\x05\x61\x63tor\x18\x02 \x01(\x0b\x32%.eigr.functions.protocol.actors.Actor\x12\x14\n\x0c\x63ommand_name\x18\x03 \x01(\t\x12#\n\x05value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05\x61sync\x18\x05 \x01(\x08\"\xb1\x01\n\x0f\x41\x63torInvocation\x12\x12\n\nactor_name\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63tor_system\x18\x02 \x01(\t\x12\x14\n\x0c\x63ommand_name\x18\x03 \x01(\t\x12\x39\n\x0f\x63urrent_context\x18\x04 \x01(\x0b\x32 .eigr.functions.protocol.Context\x12#\n\x05value\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\"\xa3\x01\n\x17\x41\x63torInvocationResponse\x12\x12\n\nactor_name\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63tor_system\x18\x02 \x01(\t\x12\x39\n\x0fupdated_context\x18\x03 \x01(\x0b\x32 .eigr.functions.protocol.Context\x12#\n\x05value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"\xe4\x01\n\x12InvocationResponse\x12\x36\n\x06status\x18\x01 \x01(\x0b\x32&.eigr.functions.protocol.RequestStatus\x12;\n\x06system\x18\x02 \x01(\x0b\x32+.eigr.functions.protocol.actors.ActorSystem\x12\x34\n\x05\x61\x63tor\x18\x03 \x01(\x0b\x32%.eigr.functions.protocol.actors.Actor\x12#\n\x05value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"Q\n\rRequestStatus\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.eigr.functions.protocol.Status\x12\x0f\n\x07message\x18\x02 \x01(\t*=\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x13\n\x0f\x41\x43TOR_NOT_FOUND\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x42O\n\x1aio.eigr.functions.protocolZ1github.com/eigr/go-support/eigr/protocol;protocolb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.eigr.functions.protocol.actors.protocol_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032io.eigr.functions.protocolZ1github.com/eigr/go-support/eigr/protocol;protocol'
  _STATUS._serialized_start=1696
  _STATUS._serialized_end=1757
  _REGISTRATIONREQUEST._serialized_start=155
  _REGISTRATIONREQUEST._serialized_end=303
  _SERVICEINFO._serialized_start=306
  _SERVICEINFO._serialized_end=518
  _PROXYINFO._serialized_start=520
  _PROXYINFO._serialized_end=638
  _REGISTRATIONRESPONSE._serialized_start=641
  _REGISTRATIONRESPONSE._serialized_end=775
  _CONTEXT._serialized_start=777
  _CONTEXT._serialized_end=823
  _INVOCATIONREQUEST._serialized_start=826
  _INVOCATIONREQUEST._serialized_end=1034
  _ACTORINVOCATION._serialized_start=1037
  _ACTORINVOCATION._serialized_end=1214
  _ACTORINVOCATIONRESPONSE._serialized_start=1217
  _ACTORINVOCATIONRESPONSE._serialized_end=1380
  _INVOCATIONRESPONSE._serialized_start=1383
  _INVOCATIONRESPONSE._serialized_end=1611
  _REQUESTSTATUS._serialized_start=1613
  _REQUESTSTATUS._serialized_end=1694
# @@protoc_insertion_point(module_scope)
