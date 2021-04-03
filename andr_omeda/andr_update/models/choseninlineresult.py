from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChosenInlineResult(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="chosen_inline_result",
        blank=True
    )
    from_user = models.OneToOneField(
        "Andruser",
        on_delete=models.CASCADE,
        blank=False
    )
    result_id = models.TextField(_("result_id"), blank=False)
    query = models.TextField(_("query"), blank=False)
    inline_message_id = models.TextField(_("inline_message_id"), blank=True)
