# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hypernets/dispatchers/grpc/proto/spec.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hypernets/dispatchers/grpc/proto/spec.proto',
  package='hypernets.dispatchers.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+hypernets/dispatchers/grpc/proto/spec.proto\x12\x1bhypernets.dispatchers.proto\"\x17\n\x07RpcCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\"\x18\n\nExecutorId\x12\n\n\x02id\x18\x01 \x01(\t\"6\n\tTrailItem\x12\x10\n\x08space_id\x18\x01 \x01(\t\x12\x17\n\x0fspace_file_path\x18\x02 \x01(\t\"\x80\x01\n\x0bTrailReport\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x04\x63ode\x18\x02 \x01(\x0b\x32$.hypernets.dispatchers.proto.RpcCode\x12\x10\n\x08space_id\x18\x03 \x01(\t\x12\x0e\n\x06reward\x18\x04 \x01(\x02\x12\x0f\n\x07message\x18\x05 \x01(\t2\xfe\x02\n\x0cSearchDriver\x12^\n\x08register\x12\'.hypernets.dispatchers.proto.ExecutorId\x1a\'.hypernets.dispatchers.proto.ExecutorId\"\x00\x12W\n\x04\x62\x65\x61t\x12\'.hypernets.dispatchers.proto.ExecutorId\x1a$.hypernets.dispatchers.proto.RpcCode\"\x00\x12Y\n\x04next\x12\'.hypernets.dispatchers.proto.ExecutorId\x1a&.hypernets.dispatchers.proto.TrailItem\"\x00\x12Z\n\x06report\x12(.hypernets.dispatchers.proto.TrailReport\x1a$.hypernets.dispatchers.proto.RpcCode\"\x00\x62\x06proto3'
)




_RPCCODE = _descriptor.Descriptor(
  name='RpcCode',
  full_name='hypernets.dispatchers.proto.RpcCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='hypernets.dispatchers.proto.RpcCode.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=76,
  serialized_end=99,
)


_EXECUTORID = _descriptor.Descriptor(
  name='ExecutorId',
  full_name='hypernets.dispatchers.proto.ExecutorId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hypernets.dispatchers.proto.ExecutorId.id', index=0,
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
  serialized_start=101,
  serialized_end=125,
)


_TRAILITEM = _descriptor.Descriptor(
  name='TrailItem',
  full_name='hypernets.dispatchers.proto.TrailItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='space_id', full_name='hypernets.dispatchers.proto.TrailItem.space_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='space_file_path', full_name='hypernets.dispatchers.proto.TrailItem.space_file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=127,
  serialized_end=181,
)


_TRAILREPORT = _descriptor.Descriptor(
  name='TrailReport',
  full_name='hypernets.dispatchers.proto.TrailReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hypernets.dispatchers.proto.TrailReport.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='hypernets.dispatchers.proto.TrailReport.code', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='space_id', full_name='hypernets.dispatchers.proto.TrailReport.space_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward', full_name='hypernets.dispatchers.proto.TrailReport.reward', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='hypernets.dispatchers.proto.TrailReport.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=184,
  serialized_end=312,
)

_TRAILREPORT.fields_by_name['code'].message_type = _RPCCODE
DESCRIPTOR.message_types_by_name['RpcCode'] = _RPCCODE
DESCRIPTOR.message_types_by_name['ExecutorId'] = _EXECUTORID
DESCRIPTOR.message_types_by_name['TrailItem'] = _TRAILITEM
DESCRIPTOR.message_types_by_name['TrailReport'] = _TRAILREPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RpcCode = _reflection.GeneratedProtocolMessageType('RpcCode', (_message.Message,), {
  'DESCRIPTOR' : _RPCCODE,
  '__module__' : 'hypernets.dispatchers.grpc.proto.spec_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.proto.RpcCode)
  })
_sym_db.RegisterMessage(RpcCode)

ExecutorId = _reflection.GeneratedProtocolMessageType('ExecutorId', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTORID,
  '__module__' : 'hypernets.dispatchers.grpc.proto.spec_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.proto.ExecutorId)
  })
_sym_db.RegisterMessage(ExecutorId)

TrailItem = _reflection.GeneratedProtocolMessageType('TrailItem', (_message.Message,), {
  'DESCRIPTOR' : _TRAILITEM,
  '__module__' : 'hypernets.dispatchers.grpc.proto.spec_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.proto.TrailItem)
  })
_sym_db.RegisterMessage(TrailItem)

TrailReport = _reflection.GeneratedProtocolMessageType('TrailReport', (_message.Message,), {
  'DESCRIPTOR' : _TRAILREPORT,
  '__module__' : 'hypernets.dispatchers.grpc.proto.spec_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.proto.TrailReport)
  })
_sym_db.RegisterMessage(TrailReport)



_SEARCHDRIVER = _descriptor.ServiceDescriptor(
  name='SearchDriver',
  full_name='hypernets.dispatchers.proto.SearchDriver',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=315,
  serialized_end=697,
  methods=[
  _descriptor.MethodDescriptor(
    name='register',
    full_name='hypernets.dispatchers.proto.SearchDriver.register',
    index=0,
    containing_service=None,
    input_type=_EXECUTORID,
    output_type=_EXECUTORID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='beat',
    full_name='hypernets.dispatchers.proto.SearchDriver.beat',
    index=1,
    containing_service=None,
    input_type=_EXECUTORID,
    output_type=_RPCCODE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='next',
    full_name='hypernets.dispatchers.proto.SearchDriver.next',
    index=2,
    containing_service=None,
    input_type=_EXECUTORID,
    output_type=_TRAILITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='report',
    full_name='hypernets.dispatchers.proto.SearchDriver.report',
    index=3,
    containing_service=None,
    input_type=_TRAILREPORT,
    output_type=_RPCCODE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHDRIVER)

DESCRIPTOR.services_by_name['SearchDriver'] = _SEARCHDRIVER

# @@protoc_insertion_point(module_scope)
