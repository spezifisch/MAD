# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/messages/send_facebook_friend_invite_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/messages/send_facebook_friend_invite_message.proto',
  package='pogoprotos.networking.social.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nOpogoprotos/networking/social/messages/send_facebook_friend_invite_message.proto\x12%pogoprotos.networking.social.messages\"U\n\x1fSendFacebookFriendInviteMessage\x12\x17\n\x0f\x66\x62_access_token\x18\x01 \x01(\t\x12\x19\n\x11\x66riend_fb_user_id\x18\x02 \x01(\tb\x06proto3'
)




_SENDFACEBOOKFRIENDINVITEMESSAGE = _descriptor.Descriptor(
  name='SendFacebookFriendInviteMessage',
  full_name='pogoprotos.networking.social.messages.SendFacebookFriendInviteMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fb_access_token', full_name='pogoprotos.networking.social.messages.SendFacebookFriendInviteMessage.fb_access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_fb_user_id', full_name='pogoprotos.networking.social.messages.SendFacebookFriendInviteMessage.friend_fb_user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=122,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['SendFacebookFriendInviteMessage'] = _SENDFACEBOOKFRIENDINVITEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendFacebookFriendInviteMessage = _reflection.GeneratedProtocolMessageType('SendFacebookFriendInviteMessage', (_message.Message,), {
  'DESCRIPTOR' : _SENDFACEBOOKFRIENDINVITEMESSAGE,
  '__module__' : 'pogoprotos.networking.social.messages.send_facebook_friend_invite_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.messages.SendFacebookFriendInviteMessage)
  })
_sym_db.RegisterMessage(SendFacebookFriendInviteMessage)


# @@protoc_insertion_point(module_scope)