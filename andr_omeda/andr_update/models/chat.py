from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Chat(models.Model):
    chat_id = models.BigIntegerField(_("chat_id"), blank=False, primary_key=True, default=0)
    type = models.TextField(_("type"), blank=False)
    title = models.TextField(_("type"), blank=True)
    username = models.TextField(_("username"), blank=True)
    first_name = models.TextField(_("first_name"), blank=True)
    last_name = models.TextField(_("last_name"), blank=True)
    bio = models.TextField(_("bio"), blank=True)
    description = models.TextField(_("description"), blank=True)
    invite_link = models.TextField(_("invite_link"), blank=True)
    slow_mode_delay = models.IntegerField(_("slow_mode_delay"), blank=True, null=True)
    sticker_set_name = models.TextField(_("sticker_set_name"), blank=True)
    can_set_sticker_set = models.BooleanField(_("can_set_sticker_set"), blank=True, null=True)
    linked_chat_id = models.BigIntegerField(_("linked_chat_id"), blank=True, null=True)
    # TODO [WORKAROUND20032208]
    pinned_message = models.JSONField(_("pinned_message"), default=dict, blank=True)

    def geet_message(self):
        return self.message
    
    def __str__(self):
        if self.chat_id:
            return "Chat with pgId: %i" % self.chat_id

    @classmethod
    def get_message_with_id_in_chat_with_id(cls, chat_id, message_id):
        try:
            chat = cls.objects.get(chat_id=chat_id)
            message = chat.message
            return chat
        except cls.DoesNotExist:
            raise cls.DoesNotExist

    @classmethod
    def chat_with_id_exists(cls, chat_id):
        return cls.objects.filter(pk=chat_id).exists()

    @classmethod
    def get_chat_with_id(cls, chat_id=None):
        
        if not chat_id:
            return None
        if cls.chat_with_id_exists(chat_id):
            return cls.objects.get(pk=chat_id)
        else:
            return None
    
    @classmethod
    def context_chat_unicity_check(cls, data):
        if not data.get('chat', None):
            raise Exception("KeyError chat not present in data")
        _id = data['chat'].get('chat_id', None)
        if not _id:
            raise Exception("KeyError something wrong with chat_id")
        chat = cls.get_chat_with_id(chat_id=_id)
        if chat:
            data.pop('chat', None)
            context = {'validated_data': data, 'chat': chat.chat_id}
        else:
            context = {'validated_data': data}
        
        return context

    @classmethod
    def context_chat_unicity_check_for_field(cls, data, field=''):
        if not data.get(field, None):
            raise Exception("KeyError chat not present in data")
        _id = data[field].get('chat_id', None)
        if not _id:
            raise Exception("KeyError something wrong with chat_id")
        chat = cls.get_chat_with_id(chat_id=_id)
        if chat:
            data.pop(field)
            context = {'validated_data': data, 'chat': chat.chat_id}
        else:
            context = {'validated_data': data}
        
        return context

    @classmethod
    def context_chat_unicity_check_for_field_and_context(cls, data, unicity, field='', prefix=''):
        """
        data: message => {..., 'chat': {'chat_id':10000, ...}}
        field: 'chat'
        prefix: message
        """
        if not data.get(field, None):
            return unicity

        _id = data[field].get('id', None)
        if not _id:
            raise Exception("KeyError something wrong with chat_id")
        
        chat = cls.get_chat_with_id(chat_id=_id)
        if chat:
            del data[field]
            unicity[prefix + '__' + field] = chat.chat_id
        else:
            data[field]['chat_id'] = data[field]['id']
            del data[field]['id']
        
        return unicity
    
    
