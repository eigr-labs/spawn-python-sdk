# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: domain/domain.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='domain/domain.proto',
  package='domain',
  syntax='proto3',
  serialized_options=b'\n\"eigr.functions.spawn.example.stateB\022JoeStateStateProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x64omain/domain.proto\x12\x06\x64omain\"\x1d\n\x08JoeState\x12\x11\n\tlanguages\x18\x01 \x03(\t\"\x1b\n\x07Request\x12\x10\n\x08language\x18\x01 \x01(\t\"\x19\n\x05Reply\x12\x10\n\x08response\x18\x01 \x01(\tB:\n\"eigr.functions.spawn.example.stateB\x12JoeStateStateProtoP\x01\x62\x06proto3'
)




_JOESTATE = _descriptor.Descriptor(
  name='JoeState',
  full_name='domain.JoeState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='languages', full_name='domain.JoeState.languages', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=60,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='domain.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='domain.Request.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=89,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='domain.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='domain.Reply.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['JoeState'] = _JOESTATE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JoeState = _reflection.GeneratedProtocolMessageType('JoeState', (_message.Message,), {
  'DESCRIPTOR' : _JOESTATE,
  '__module__' : 'domain.domain_pb2'
  # @@protoc_insertion_point(class_scope:domain.JoeState)
  })
_sym_db.RegisterMessage(JoeState)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'domain.domain_pb2'
  # @@protoc_insertion_point(class_scope:domain.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'domain.domain_pb2'
  # @@protoc_insertion_point(class_scope:domain.Reply)
  })
_sym_db.RegisterMessage(Reply)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
