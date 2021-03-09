from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Chat


class ChatPermissions(models.Model):
    chat = models.OneToOneField(
        Chat,
        on_delete=models.CASCADE,
        related_name="permissions",
        blank=True
    )
    can_send_messages = models.BooleanField(_("can_send_messages"), blank=True)
    can_send_media_messages = models.BooleanField(_("can_send_media_messages"), blank=True)
    can_send_polls = models.BooleanField(_("can_send_polls"), blank=True)
    can_send_other_messages = models.BooleanField(_("can_send_other_messages"), blank=True)
    can_add_web_page_previews = models.BooleanField(_("can_add_web_page_previews"), blank=True)
    can_change_info = models.BooleanField(_("can_change_info"), blank=True)
    can_invite_users = models.BooleanField(_("can_invite_users"), blank=True)
    can_pin_messages = models.BooleanField(_("can_pin_messages"), blank=True)
