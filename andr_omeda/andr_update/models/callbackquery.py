from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class CallbackQuery(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE
        related_name="callback_query"
        blank=True
    )
    id = models.CharField(_("id"), blank=False)
    inline_message_id = models.CharField(_("inline_message_id"), blank=True)
    chat_instance = models.CharField(_("chat_instance"), blank=True)
    data = models.CharField(_("data"), blank=True)
    game_short_name = models.CharField(_("game_short_name"), blank=True)
