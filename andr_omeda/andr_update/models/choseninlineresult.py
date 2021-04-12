from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChosenInlineResult(models.Model):
    from_user = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        related_name="chosen_inline_results",
        blank=False,
        null=True
    )
    result_id = models.TextField(_("result_id"), blank=False)
    query = models.TextField(_("query"), blank=False)
    inline_message_id = models.TextField(_("inline_message_id"), blank=True)
