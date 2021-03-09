from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, InlineKeyboardButton


class CallbackGame(models.Model):
    """placeholder"""
    inline_keyboard_button = models.OneToOneField(
        InlineKeyboardButton,
        on_delete=models.CASCADE,
        related_name="callback_game",
        blank=True
    )
