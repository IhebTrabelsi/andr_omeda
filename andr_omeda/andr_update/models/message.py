from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import AndrUser, Chat


class Message(models.Model):
    message_id = models.IntegerField(_("message_id"), blank=False)
    this_pinned_message_chat = models.OneToOneField(
        Chat,
        on_delete=models.CASCADE,
        related_name="pinned_message"
        blank=True
    )
    reply_to_message = models.OneToOneField(
        "self",
        on_delete=models.DO_NOTHING,
        blank=True
    )
    pinned_message = models.OneToOneField(
        "self",
        on_delete=models.DO_NOTHING,
        blank=True
    )

    date = models.IntegerField(_("date"), blank=False)
    forward_from_message_id = models.IntegerField(_("forward_from_message_id"), blank=True)
    forward_signature = models.CharField(_("forward_signature"), blank=True)
    forward_sender_name = models.CharField(_("forward_sender_name"), blank=True)
    forward_date = models.IntegerField(_("forward_date"), blank=True)
    edit_date = models.IntegerField(_("edit_date"), blank=True)
    media_group_id = models.CharField(_("media_group_id"), blank=True)
    author_signature = models.CharField(_("author_signature"), blank=True)
    text = models.CharField(
        _("text"),
        max_length=4096
        blank=True
    )
    caption = models.CharField(
        _("caption"),
        max_length=1024
        blank=True
    )
    new_chat_title = models.CharField(_("new_chat_title"), blank=True)
    delete_chat_photo = models.BooleanField(_("delete_chat_photo"), blank=True)
    group_chat_created = models.BooleanField(_("group_chat_created"), blank=True)
    supergroup_chat_created = models.BooleanField(_("supergroup_chat_created"), blank=True)
    channel_chat_created = models.BooleanField(_("channel_chat_created"), blank=True)
    migrate_to_chat_id = models.BigIntegerField(_("migrate_to_chat_id"), blank=True)
    migrate_from_chat_id = models.BigIntegerField(_("migrate_from_chat_id"), blank=True)
    connected_website = models.CharField(_("connected_website"), blank=True)
