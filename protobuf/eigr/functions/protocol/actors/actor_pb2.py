# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/eigr/functions/protocol/actors/actor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3protobuf/eigr/functions/protocol/actors/actor.proto\x12\x1e\x65igr.functions.protocol.actors\x1a\x19google/protobuf/any.proto\"\xa6\x01\n\x08Registry\x12\x44\n\x06\x61\x63tors\x18\x01 \x03(\x0b\x32\x34.eigr.functions.protocol.actors.Registry.ActorsEntry\x1aT\n\x0b\x41\x63torsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.eigr.functions.protocol.actors.Actor:\x02\x38\x01\"W\n\x0b\x41\x63torSystem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x08registry\x18\x02 \x01(\x0b\x32(.eigr.functions.protocol.actors.Registry\"g\n\x15\x41\x63torSnapshotStrategy\x12\x42\n\x07timeout\x18\x01 \x01(\x0b\x32/.eigr.functions.protocol.actors.TimeoutStrategyH\x00\x42\n\n\x08strategy\"i\n\x17\x41\x63torDeactivateStrategy\x12\x42\n\x07timeout\x18\x01 \x01(\x0b\x32/.eigr.functions.protocol.actors.TimeoutStrategyH\x00\x42\n\n\x08strategy\"\"\n\x0fTimeoutStrategy\x12\x0f\n\x07timeout\x18\x01 \x01(\x03\"\xa2\x01\n\nActorState\x12\x42\n\x04tags\x18\x01 \x03(\x0b\x32\x34.eigr.functions.protocol.actors.ActorState.TagsEntry\x12#\n\x05state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x02\n\x05\x41\x63tor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\npersistent\x18\x02 \x01(\x08\x12\x39\n\x05state\x18\x03 \x01(\x0b\x32*.eigr.functions.protocol.actors.ActorState\x12P\n\x11snapshot_strategy\x18\x04 \x01(\x0b\x32\x35.eigr.functions.protocol.actors.ActorSnapshotStrategy\x12T\n\x13\x64\x65\x61\x63tivate_strategy\x18\x05 \x01(\x0b\x32\x37.eigr.functions.protocol.actors.ActorDeactivateStrategyBR\n!io.eigr.functions.protocol.actorsZ-github.com/eigr/go-support/eigr/actors;actorsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.eigr.functions.protocol.actors.actor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.eigr.functions.protocol.actorsZ-github.com/eigr/go-support/eigr/actors;actors'
  _REGISTRY_ACTORSENTRY._options = None
  _REGISTRY_ACTORSENTRY._serialized_options = b'8\001'
  _ACTORSTATE_TAGSENTRY._options = None
  _ACTORSTATE_TAGSENTRY._serialized_options = b'8\001'
  _REGISTRY._serialized_start=115
  _REGISTRY._serialized_end=281
  _REGISTRY_ACTORSENTRY._serialized_start=197
  _REGISTRY_ACTORSENTRY._serialized_end=281
  _ACTORSYSTEM._serialized_start=283
  _ACTORSYSTEM._serialized_end=370
  _ACTORSNAPSHOTSTRATEGY._serialized_start=372
  _ACTORSNAPSHOTSTRATEGY._serialized_end=475
  _ACTORDEACTIVATESTRATEGY._serialized_start=477
  _ACTORDEACTIVATESTRATEGY._serialized_end=582
  _TIMEOUTSTRATEGY._serialized_start=584
  _TIMEOUTSTRATEGY._serialized_end=618
  _ACTORSTATE._serialized_start=621
  _ACTORSTATE._serialized_end=783
  _ACTORSTATE_TAGSENTRY._serialized_start=740
  _ACTORSTATE_TAGSENTRY._serialized_end=783
  _ACTOR._serialized_start=786
  _ACTOR._serialized_end=1054
# @@protoc_insertion_point(module_scope)