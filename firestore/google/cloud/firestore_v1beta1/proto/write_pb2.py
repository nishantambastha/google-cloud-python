# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/firestore_v1beta1/proto/write.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.firestore_v1beta1.proto import common_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_common__pb2
from google.cloud.firestore_v1beta1.proto import document_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/firestore_v1beta1/proto/write.proto',
  package='google.firestore.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n0google/cloud/firestore_v1beta1/proto/write.proto\x12\x18google.firestore.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x31google/cloud/firestore_v1beta1/proto/common.proto\x1a\x33google/cloud/firestore_v1beta1/proto/document.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9d\x02\n\x05Write\x12\x34\n\x06update\x18\x01 \x01(\x0b\x32\".google.firestore.v1beta1.DocumentH\x00\x12\x10\n\x06\x64\x65lete\x18\x02 \x01(\tH\x00\x12@\n\ttransform\x18\x06 \x01(\x0b\x32+.google.firestore.v1beta1.DocumentTransformH\x00\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32&.google.firestore.v1beta1.DocumentMask\x12@\n\x10\x63urrent_document\x18\x04 \x01(\x0b\x32&.google.firestore.v1beta1.PreconditionB\x0b\n\toperation\"\xda\x02\n\x11\x44ocumentTransform\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12T\n\x10\x66ield_transforms\x18\x02 \x03(\x0b\x32:.google.firestore.v1beta1.DocumentTransform.FieldTransform\x1a\xdc\x01\n\x0e\x46ieldTransform\x12\x12\n\nfield_path\x18\x01 \x01(\t\x12\x65\n\x13set_to_server_value\x18\x02 \x01(\x0e\x32\x46.google.firestore.v1beta1.DocumentTransform.FieldTransform.ServerValueH\x00\"=\n\x0bServerValue\x12\x1c\n\x18SERVER_VALUE_UNSPECIFIED\x10\x00\x12\x10\n\x0cREQUEST_TIME\x10\x01\x42\x10\n\x0etransform_type\"z\n\x0bWriteResult\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x11transform_results\x18\x02 \x03(\x0b\x32\x1f.google.firestore.v1beta1.Value\"v\n\x0e\x44ocumentChange\x12\x34\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\".google.firestore.v1beta1.Document\x12\x12\n\ntarget_ids\x18\x05 \x03(\x05\x12\x1a\n\x12removed_target_ids\x18\x06 \x03(\x05\"m\n\x0e\x44ocumentDelete\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12\x1a\n\x12removed_target_ids\x18\x06 \x03(\x05\x12-\n\tread_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"m\n\x0e\x44ocumentRemove\x12\x10\n\x08\x64ocument\x18\x01 \x01(\t\x12\x1a\n\x12removed_target_ids\x18\x02 \x03(\x05\x12-\n\tread_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"3\n\x0f\x45xistenceFilter\x12\x11\n\ttarget_id\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x42\x97\x01\n\x1c\x63om.google.firestore.v1beta1B\nWriteProtoP\x01ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_common__pb2.DESCRIPTOR,google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE = _descriptor.EnumDescriptor(
  name='ServerValue',
  full_name='google.firestore.v1beta1.DocumentTransform.FieldTransform.ServerValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVER_VALUE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_TIME', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=801,
  serialized_end=862,
)
_sym_db.RegisterEnumDescriptor(_DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE)


_WRITE = _descriptor.Descriptor(
  name='Write',
  full_name='google.firestore.v1beta1.Write',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='google.firestore.v1beta1.Write.update', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete', full_name='google.firestore.v1beta1.Write.delete', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transform', full_name='google.firestore.v1beta1.Write.transform', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.firestore.v1beta1.Write.update_mask', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_document', full_name='google.firestore.v1beta1.Write.current_document', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.firestore.v1beta1.Write.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=246,
  serialized_end=531,
)


_DOCUMENTTRANSFORM_FIELDTRANSFORM = _descriptor.Descriptor(
  name='FieldTransform',
  full_name='google.firestore.v1beta1.DocumentTransform.FieldTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_path', full_name='google.firestore.v1beta1.DocumentTransform.FieldTransform.field_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_to_server_value', full_name='google.firestore.v1beta1.DocumentTransform.FieldTransform.set_to_server_value', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='transform_type', full_name='google.firestore.v1beta1.DocumentTransform.FieldTransform.transform_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=660,
  serialized_end=880,
)

_DOCUMENTTRANSFORM = _descriptor.Descriptor(
  name='DocumentTransform',
  full_name='google.firestore.v1beta1.DocumentTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='google.firestore.v1beta1.DocumentTransform.document', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_transforms', full_name='google.firestore.v1beta1.DocumentTransform.field_transforms', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DOCUMENTTRANSFORM_FIELDTRANSFORM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=880,
)


_WRITERESULT = _descriptor.Descriptor(
  name='WriteResult',
  full_name='google.firestore.v1beta1.WriteResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.firestore.v1beta1.WriteResult.update_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transform_results', full_name='google.firestore.v1beta1.WriteResult.transform_results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=1004,
)


_DOCUMENTCHANGE = _descriptor.Descriptor(
  name='DocumentChange',
  full_name='google.firestore.v1beta1.DocumentChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='google.firestore.v1beta1.DocumentChange.document', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_ids', full_name='google.firestore.v1beta1.DocumentChange.target_ids', index=1,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='removed_target_ids', full_name='google.firestore.v1beta1.DocumentChange.removed_target_ids', index=2,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1006,
  serialized_end=1124,
)


_DOCUMENTDELETE = _descriptor.Descriptor(
  name='DocumentDelete',
  full_name='google.firestore.v1beta1.DocumentDelete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='google.firestore.v1beta1.DocumentDelete.document', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='removed_target_ids', full_name='google.firestore.v1beta1.DocumentDelete.removed_target_ids', index=1,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_time', full_name='google.firestore.v1beta1.DocumentDelete.read_time', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1126,
  serialized_end=1235,
)


_DOCUMENTREMOVE = _descriptor.Descriptor(
  name='DocumentRemove',
  full_name='google.firestore.v1beta1.DocumentRemove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='google.firestore.v1beta1.DocumentRemove.document', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='removed_target_ids', full_name='google.firestore.v1beta1.DocumentRemove.removed_target_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_time', full_name='google.firestore.v1beta1.DocumentRemove.read_time', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1237,
  serialized_end=1346,
)


_EXISTENCEFILTER = _descriptor.Descriptor(
  name='ExistenceFilter',
  full_name='google.firestore.v1beta1.ExistenceFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_id', full_name='google.firestore.v1beta1.ExistenceFilter.target_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='google.firestore.v1beta1.ExistenceFilter.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1348,
  serialized_end=1399,
)

_WRITE.fields_by_name['update'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2._DOCUMENT
_WRITE.fields_by_name['transform'].message_type = _DOCUMENTTRANSFORM
_WRITE.fields_by_name['update_mask'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_common__pb2._DOCUMENTMASK
_WRITE.fields_by_name['current_document'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_common__pb2._PRECONDITION
_WRITE.oneofs_by_name['operation'].fields.append(
  _WRITE.fields_by_name['update'])
_WRITE.fields_by_name['update'].containing_oneof = _WRITE.oneofs_by_name['operation']
_WRITE.oneofs_by_name['operation'].fields.append(
  _WRITE.fields_by_name['delete'])
_WRITE.fields_by_name['delete'].containing_oneof = _WRITE.oneofs_by_name['operation']
_WRITE.oneofs_by_name['operation'].fields.append(
  _WRITE.fields_by_name['transform'])
_WRITE.fields_by_name['transform'].containing_oneof = _WRITE.oneofs_by_name['operation']
_DOCUMENTTRANSFORM_FIELDTRANSFORM.fields_by_name['set_to_server_value'].enum_type = _DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE
_DOCUMENTTRANSFORM_FIELDTRANSFORM.containing_type = _DOCUMENTTRANSFORM
_DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE.containing_type = _DOCUMENTTRANSFORM_FIELDTRANSFORM
_DOCUMENTTRANSFORM_FIELDTRANSFORM.oneofs_by_name['transform_type'].fields.append(
  _DOCUMENTTRANSFORM_FIELDTRANSFORM.fields_by_name['set_to_server_value'])
_DOCUMENTTRANSFORM_FIELDTRANSFORM.fields_by_name['set_to_server_value'].containing_oneof = _DOCUMENTTRANSFORM_FIELDTRANSFORM.oneofs_by_name['transform_type']
_DOCUMENTTRANSFORM.fields_by_name['field_transforms'].message_type = _DOCUMENTTRANSFORM_FIELDTRANSFORM
_WRITERESULT.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WRITERESULT.fields_by_name['transform_results'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2._VALUE
_DOCUMENTCHANGE.fields_by_name['document'].message_type = google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2._DOCUMENT
_DOCUMENTDELETE.fields_by_name['read_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DOCUMENTREMOVE.fields_by_name['read_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Write'] = _WRITE
DESCRIPTOR.message_types_by_name['DocumentTransform'] = _DOCUMENTTRANSFORM
DESCRIPTOR.message_types_by_name['WriteResult'] = _WRITERESULT
DESCRIPTOR.message_types_by_name['DocumentChange'] = _DOCUMENTCHANGE
DESCRIPTOR.message_types_by_name['DocumentDelete'] = _DOCUMENTDELETE
DESCRIPTOR.message_types_by_name['DocumentRemove'] = _DOCUMENTREMOVE
DESCRIPTOR.message_types_by_name['ExistenceFilter'] = _EXISTENCEFILTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Write = _reflection.GeneratedProtocolMessageType('Write', (_message.Message,), dict(
  DESCRIPTOR = _WRITE,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """A write on a document.
  
  
  Attributes:
      operation:
          The operation to execute.
      update:
          A document to write.
      delete:
          A document name to delete. In the format: ``projects/{project_
          id}/databases/{database_id}/documents/{document_path}``.
      transform:
          Applies a tranformation to a document. At most one
          ``transform`` per document is allowed in a given request. An
          ``update`` cannot follow a ``transform`` on the same document
          in a given request.
      update_mask:
          The fields to update in this write.  This field can be set
          only when the operation is ``update``. None of the field paths
          in the mask may contain a reserved name. If the document
          exists on the server and has fields not referenced in the
          mask, they are left unchanged. Fields referenced in the mask,
          but not present in the input document, are deleted from the
          document on the server. The field paths in this mask must not
          contain a reserved field name.
      current_document:
          An optional precondition on the document.  The write will fail
          if this is set and not met by the target document.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.Write)
  ))
_sym_db.RegisterMessage(Write)

DocumentTransform = _reflection.GeneratedProtocolMessageType('DocumentTransform', (_message.Message,), dict(

  FieldTransform = _reflection.GeneratedProtocolMessageType('FieldTransform', (_message.Message,), dict(
    DESCRIPTOR = _DOCUMENTTRANSFORM_FIELDTRANSFORM,
    __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
    ,
    __doc__ = """A transformation of a field of the document.
    """,
    # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.DocumentTransform.FieldTransform)
    ))
  ,
  DESCRIPTOR = _DOCUMENTTRANSFORM,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """A transformation of a document.
  
  
  Attributes:
      field_path:
          The path of the field. See
          [Document.fields][google.firestore.v1beta1.Document.fields]
          for the field path syntax reference.
      transform_type:
          The transformation to apply on the field.
      set_to_server_value:
          Sets the field to the given server value.
      document:
          The name of the document to transform.
      field_transforms:
          The list of transformations to apply to the fields of the
          document, in order.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.DocumentTransform)
  ))
_sym_db.RegisterMessage(DocumentTransform)
_sym_db.RegisterMessage(DocumentTransform.FieldTransform)

WriteResult = _reflection.GeneratedProtocolMessageType('WriteResult', (_message.Message,), dict(
  DESCRIPTOR = _WRITERESULT,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """The result of applying a write.
  
  
  Attributes:
      update_time:
          The last update time of the document after applying the write.
          Not set after a ``delete``.  If the write did not actually
          change the document, this will be the previous update\_time.
      transform_results:
          The results of applying each [DocumentTransform.FieldTransform
          ][google.firestore.v1beta1.DocumentTransform.FieldTransform],
          in the same order.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.WriteResult)
  ))
_sym_db.RegisterMessage(WriteResult)

DocumentChange = _reflection.GeneratedProtocolMessageType('DocumentChange', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTCHANGE,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """A [Document][google.firestore.v1beta1.Document] has changed.
  
  May be the result of multiple [writes][google.firestore.v1beta1.Write],
  including deletes, that ultimately resulted in a new value for the
  [Document][google.firestore.v1beta1.Document].
  
  Multiple [DocumentChange][google.firestore.v1beta1.DocumentChange]
  messages may be returned for the same logical change, if multiple
  targets are affected.
  
  
  Attributes:
      document:
          The new state of the
          [Document][google.firestore.v1beta1.Document].  If ``mask`` is
          set, contains only fields that were updated or added.
      target_ids:
          A set of target IDs of targets that match this document.
      removed_target_ids:
          A set of target IDs for targets that no longer match this
          document.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.DocumentChange)
  ))
_sym_db.RegisterMessage(DocumentChange)

DocumentDelete = _reflection.GeneratedProtocolMessageType('DocumentDelete', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTDELETE,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """A [Document][google.firestore.v1beta1.Document] has been deleted.
  
  May be the result of multiple [writes][google.firestore.v1beta1.Write],
  including updates, the last of which deleted the
  [Document][google.firestore.v1beta1.Document].
  
  Multiple [DocumentDelete][google.firestore.v1beta1.DocumentDelete]
  messages may be returned for the same logical delete, if multiple
  targets are affected.
  
  
  Attributes:
      document:
          The resource name of the
          [Document][google.firestore.v1beta1.Document] that was
          deleted.
      removed_target_ids:
          A set of target IDs for targets that previously matched this
          entity.
      read_time:
          The read timestamp at which the delete was observed.  Greater
          or equal to the ``commit_time`` of the delete.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.DocumentDelete)
  ))
_sym_db.RegisterMessage(DocumentDelete)

DocumentRemove = _reflection.GeneratedProtocolMessageType('DocumentRemove', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTREMOVE,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """A [Document][google.firestore.v1beta1.Document] has been removed from
  the view of the targets.
  
  Sent if the document is no longer relevant to a target and is out of
  view. Can be sent instead of a DocumentDelete or a DocumentChange if the
  server can not send the new value of the document.
  
  Multiple [DocumentRemove][google.firestore.v1beta1.DocumentRemove]
  messages may be returned for the same logical write or delete, if
  multiple targets are affected.
  
  
  Attributes:
      document:
          The resource name of the
          [Document][google.firestore.v1beta1.Document] that has gone
          out of view.
      removed_target_ids:
          A set of target IDs for targets that previously matched this
          document.
      read_time:
          The read timestamp at which the remove was observed.  Greater
          or equal to the ``commit_time`` of the change/delete/remove.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.DocumentRemove)
  ))
_sym_db.RegisterMessage(DocumentRemove)

ExistenceFilter = _reflection.GeneratedProtocolMessageType('ExistenceFilter', (_message.Message,), dict(
  DESCRIPTOR = _EXISTENCEFILTER,
  __module__ = 'google.cloud.firestore_v1beta1.proto.write_pb2'
  ,
  __doc__ = """A digest of all the documents that match a given target.
  
  
  Attributes:
      target_id:
          The target ID to which this filter applies.
      count:
          The total count of documents that match [target\_id][google.fi
          restore.v1beta1.ExistenceFilter.target\_id].  If different
          from the count of documents in the client that match, the
          client must manually determine which documents no longer match
          the target.
  """,
  # @@protoc_insertion_point(class_scope:google.firestore.v1beta1.ExistenceFilter)
  ))
_sym_db.RegisterMessage(ExistenceFilter)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.google.firestore.v1beta1B\nWriteProtoP\001ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\242\002\004GCFS\252\002\036Google.Cloud.Firestore.V1Beta1'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)