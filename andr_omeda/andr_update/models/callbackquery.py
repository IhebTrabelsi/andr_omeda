from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class CallbackQuery(models.Model):
    callback_query_id = models.TextField(_("callback_query_id"), blank=False)
    inline_message_id = models.TextField(_("inline_message_id"), blank=True)
    chat_instance = models.TextField(_("chat_instance"), blank=True)
    data = models.TextField(_("data"), blank=True)
    game_short_name = models.TextField(_("game_short_name"), blank=True)
