from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, InlineKeyboardButton


class LoginUrl(models.Model):
    inline_keyboard_button = models.OneToOneField(
        InlineKeyboardButton,
        on_delete=models.CASCADE,
        related_name="login_url",
        blank=False
    )
    url = models.CharField(_("url"), blank=False)
    forward_text = models.CharField(_("forward_text"), blank=True)
    bot_username = models.CharField(_("bot_username"), blank=True)
    request_write_access = models.BooleanField(_("request_write_access"), blank=True)
