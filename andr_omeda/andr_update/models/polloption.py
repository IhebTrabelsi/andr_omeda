from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Poll


class PollOption(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="options",
        blank=True
    )
    text = models.CharField(_("text"), max_length=100, blank=False)
    voter_count = models.IntegerField(_("voter_count"), blank=False)
