from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class PollAnswer(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="poll_answer",
        blank=True
    )
    poll_id = models.TextField(_("poll_id"), blank=False)
