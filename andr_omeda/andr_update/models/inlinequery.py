from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from andr_omeda.andr_update.models import Update


class InlineQuery(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="inline_query",
        blank=True
    )
    inline_query_id = models.TextField(_("inline_query_id"), blank=False)
    query = models.TextField(_("query"), blank=False)
    offset = models.TextField(_("offset"), blank=False)
