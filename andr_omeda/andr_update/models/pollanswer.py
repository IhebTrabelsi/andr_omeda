from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class PollAnswer(models.Model):
    from_user = models.ForeignKey(
        "Andruser",
        on_delete=models.RESTRICT,
        related_name="poll_answers",
        blank=True,
        null=True
    )
    option_ids = models.JSONField(_("option_ids"), blank=False)
    poll_id = models.TextField(_("poll_id"), blank=False)
