from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Andruser, Chat, Update, \
    CallbackQuery
"""


class Message(models.Model):
    from_user = models.ForeignKey(
        "Andruser",
        related_name="messages",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    message_id = models.IntegerField(_("message_id"), blank=False)
    """
    this_pinned_message_chat = models.OneToOneField(
        "Chat",
        on_delete=models.CASCADE,
        related_name="pinned_message",
        blank=True
    )"""
    # TODO [WORKAROUND20032208] for the present time just get pinned_message
    # of Chat model as JSON field.

    reply_to_message = models.ForeignKey(
        "self",
        on_delete=models.DO_NOTHING,
        related_name="+",
        null=True,
        blank=True
    )
    pinned_message = models.OneToOneField(
        "self",
        on_delete=models.DO_NOTHING,
        related_name="+",
        null=True,
        blank=True
    )
    callbackquery = models.OneToOneField(
        "CallbackQuery",
        on_delete=models.CASCADE,
        related_name="message",
        null=True,
        blank=True
    )
    chat = models.ForeignKey(
        "Chat",
        on_delete=models.RESTRICT,
        related_name="message",
        null=True,
        blank=True
    )
    sender_chat = models.ForeignKey(
        "Chat",
        on_delete=models.RESTRICT,
        related_name="sended_messages",
        null=True,
        blank=True
    )
    forward_from = models.ForeignKey(
        "Andruser",
        on_delete=models.RESTRICT,
        related_name="forwarded_messages",
        blank=True,
        null=True
    )
    forward_from_chat = models.ForeignKey(
        "Chat",
        on_delete=models.RESTRICT,
        related_name="forwarded_messages",
        null=True,
        blank=True
    )
    left_chat_member = models.ForeignKey(
        "Andruser",
        on_delete=models.RESTRICT,
        related_name="messages_left_from",
        blank=True,
        null=True
    )
    via_bot = models.ForeignKey(
        "Andruser",
        on_delete=models.RESTRICT,
        related_name="messages_via_this_bot",
        blank=True,
        null=True
    )

    

    date = models.IntegerField(_("date"), blank=False)
    forward_from_message_id = models.IntegerField(_("forward_from_message_id"), blank=True, null=True)
    forward_signature = models.TextField(_("forward_signature"), blank=True)
    forward_sender_name = models.TextField(_("forward_sender_name"), blank=True)
    forward_date = models.IntegerField(_("forward_date"), blank=True, null=True)
    edit_date = models.IntegerField(_("edit_date"), blank=True, null=True)
    media_group_id = models.TextField(_("media_group_id"), blank=True)
    author_signature = models.TextField(_("author_signature"), blank=True)
    text = models.CharField(
        _("text"),
        max_length=4096,
        blank=True
    )
    caption = models.CharField(
        _("caption"),
        max_length=1024,
        blank=True
    )
    new_chat_title = models.TextField(_("new_chat_title"), blank=True)
    delete_chat_photo = models.BooleanField(_("delete_chat_photo"), blank=True, null=True)
    group_chat_created = models.BooleanField(_("group_chat_created"), blank=True, null=True)
    supergroup_chat_created = models.BooleanField(_("supergroup_chat_created"), blank=True, null=True)
    channel_chat_created = models.BooleanField(_("channel_chat_created"), blank=True, null=True)
    migrate_to_chat_id = models.BigIntegerField(_("migrate_to_chat_id"), blank=True, null=True)
    migrate_from_chat_id = models.BigIntegerField(_("migrate_from_chat_id"), blank=True, null=True)
    connected_website = models.TextField(_("connected_website"), blank=True)

    @classmethod
    def get_message_with_message_id_list(cls, message_id):
        return list(cls.objects.get(message_id=message_id))

    @classmethod
    def get_message_for_message_id_and_chat_id(cls, message_id=None, chat_id=None):
        if not message_id or not chat_id:
            return None

        if cls.objects.filter(chat__chat_id=chat_id).filter(message_id=message_id).exists():
            return cls.objects.filter(chat__chat_id=chat_id).filter(message_id=message_id)[:1].get()
        else:
            return None

    @classmethod 
    def get_message_with_id_attrs(cls):
        return [['chat', 'sender_chat', 'forward_from_chat'], \
            ['from', 'from_user', 'forward_from', 'via_bot', 'left_chat_member', 'user', 'creator']]
    
    def __str__(self):
        return "Message with Id : %i in chat with id : %i" % (self.id , self.chat.chat_id)

    @classmethod 
    def extract_lists(cls, data, lists, *args, **kwargs):
        new_chat_members = data.get('new_chat_members', None)
        # del new_chat_participant/new_chat_member (buggy params) at the same spot
        if data.get('new_chat_participant', None):
            del data['new_chat_participant']
        if data.get('left_chat_participant', None):
            del data['left_chat_participant']
        if data.get('new_chat_member', None):
            del data['new_chat_member']
        if not new_chat_members == None:
            if len(new_chat_members) == 0:
                del data['new_chat_members']
            else:
                lists['message__new_chat_members'] = data['new_chat_members']
                del data['new_chat_members']
        
        return lists
    
    