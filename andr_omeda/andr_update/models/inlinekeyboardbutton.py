from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, InlineKeyboardMarkup


class InlineKeyboardButton(models.Model):
    # TODO see if there is a better solution to repr
    # an array to array in django relationships
    markup = models.ManyToManyField(
        InlineKeyboardMarkup,
        related_name="inline_keyboard",
        blank=False
    )
    buttons = models.ManyToManyField(
        "self",
        related_name="buttons",
        blank=True
    )
    text = models.TextField(_("text"), blank=False)
    url = models.TextField(_("url"), blank=True)
    callback_data = models.CharField(_("callback_data"), max_length=64, blank=True)
    switch_inline_query = models.TextField(_("switch_inline_query"), blank=True)
    switch_inline_query_current_chat = models.TextField(_("switch_inline_query_current_chat"), blank=True)
    pay = models.BooleanField(_("pay"), blank=True)
