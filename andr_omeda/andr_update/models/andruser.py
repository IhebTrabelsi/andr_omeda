from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, ProximityAlertTriggered


class AndrUser(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="from",
        blank=True
    )
    forwarder = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="forward_from",
        blank=True
    )
    bot_sender = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="via_bot",
        blank=True
    )
    entity_mention = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="user",
        blank=True
    )
    chat_members_message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="new_chat_members",
        blank=True
    )
    chat_leaving_member_message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="left_chat_member",
        blank=True
    )
    proximity_alert_for_traveler = models.OneToOneField(
        ProximityAlertTriggered,
        on_delete=models.CASCADE,
        related_name="traveler",
        blank=False
    )
    proximity_alert_for_watcher = models.OneToOneField(
        ProximityAlertTriggered,
        on_delete=models.CASCADE,
        related_name="watcher",
        blank=False
    )

    user_id = models.IntegerField(_("user_id"), blank=False)
    is_bot = models.BooleanField(_("is_bot"), blank=False)
    first_name = models.CharField(_("first_name"), blank=False)
    last_name = models.CharField(_("last_name"), blank=True)
    username = models.CharField(_("username"), blank=True)
    language_code = models.CharField(_("language_code"), blank=True)
    can_join_groups = models.BooleanField(_("can_join_groups"), blank=True)
    can_read_all_group_messages = models.BooleanField(_("can_read_all_group_messages"), blank=True)
    supports_inline_queries = models.BooleanField(_("supports_inline_queries"), blank=True)
