from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import PollAnswer


class PollAnswerOptionsId(models.Model):
    poll_answers = models.ManyToManyField(
        PollAnswer,
        related_name="option_ids",
        blank=False
    )
    identifier_value = models.IntegerField(_(""), blank=False, null=True)
