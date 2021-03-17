from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Andruser, Chat, Update, \
    CallbackQuery
"""


class Message(models.Model):
    message_id = models.IntegerField(_("message_id"), blank=False)
    this_pinned_message_chat = models.OneToOneField(
        "Chat",
        on_delete=models.CASCADE,
        related_name="pinned_message",
        blank=True
    )
    reply_to_message = models.OneToOneField(
        "self",
        on_delete=models.DO_NOTHING,
        related_name="+",
        blank=True
    )
    pinned_message = models.OneToOneField(
        "self",
        on_delete=models.DO_NOTHING,
        related_name="+",
        blank=True
    )
    update = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        related_name="message",
        blank=True
    )
    update_for_this_edited_message = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        related_name="edited_message",
        blank=True
    )
    update_for_this_channel_post = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        related_name="channel_post",
        blank=True
    )
    update_for_this_edited_channel_post = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        related_name="edited_channel_post",
        blank=True
    )
    callbackquery = models.OneToOneField(
        "CallbackQuery",
        on_delete=models.CASCADE,
        related_name="message",
        blank=True
    )
    chat = models.ForeignKey(
        "Chat",
        on_delete=models.RESTRICT,
        related_name="message",
        blank=False
    )
    sender_chat = models.ForeignKey(
        "Chat",
        on_delete=models.RESTRICT,
        blank=True
    )
    forward_from_chat = models.ForeignKey(
        "Chat",
        on_delete=models.RESTRICT,
        blank=True
    )

    date = models.IntegerField(_("date"), blank=False)
    forward_from_message_id = models.IntegerField(_("forward_from_message_id"), blank=True)
    forward_signature = models.TextField(_("forward_signature"), blank=True)
    forward_sender_name = models.TextField(_("forward_sender_name"), blank=True)
    forward_date = models.IntegerField(_("forward_date"), blank=True)
    edit_date = models.IntegerField(_("edit_date"), blank=True)
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
    delete_chat_photo = models.BooleanField(_("delete_chat_photo"), blank=True)
    group_chat_created = models.BooleanField(_("group_chat_created"), blank=True)
    supergroup_chat_created = models.BooleanField(_("supergroup_chat_created"), blank=True)
    channel_chat_created = models.BooleanField(_("channel_chat_created"), blank=True)
    migrate_to_chat_id = models.BigIntegerField(_("migrate_to_chat_id"), blank=True)
    migrate_from_chat_id = models.BigIntegerField(_("migrate_from_chat_id"), blank=True)
    connected_website = models.TextField(_("connected_website"), blank=True)

    @classmethod
    def get_message_with_message_id_list(cls, message_id):
        return list(cls.objects.get(message_id=message_id))
