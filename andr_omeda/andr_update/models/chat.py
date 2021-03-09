from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Chat(models.Model):
    chat_id = models.BigIntegerField(_("chat_id"), blank=False)
    type = models.TextField(_("type"), blank=False)
    title = models.TextField(_("type"), blank=True)
    username = models.TextField(_("username"), blank=True)
    first_name = models.TextField(_("first_name"), blank=True)
    last_name = models.TextField(_("last_name"), blank=True)
    bio = models.TextField(_("bio"), blank=True)
    description = models.TextField(_("description"), blank=True)
    invite_link = models.TextField(_("invite_link"), blank=True)
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="chat",
        blank=True
    )
    receiver_message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="sender_chat",
        blank=True
    )
    forwarder_chat = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="forward_from_chat",
        blank=True
    )

    slow_mode_delay = models.IntegerField(_("slow_mode_delay"), blank=True)
    sticker_set_name = models.TextField(_("sticker_set_name"), blank=True)
    can_set_sticker_set = models.BooleanField(_("can_set_sticker_set"), blank=True)
    linked_chat_id = models.BigIntegerField(_("linked_chat_id"), blank=True)
