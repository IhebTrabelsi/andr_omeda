from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class PollAnswer(models.Model):
    user = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        blank=False
    )
    option_ids = models.JSONField(_("option_ids"), blank=False)
    poll_id = models.TextField(_("poll_id"), blank=False)
