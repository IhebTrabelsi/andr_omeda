from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Dice(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="dice",
        blank=True
    )
    emoji = models.TextField(_("emoji"), blank=False)
    value = models.IntegerField(_("value"), blank=False)
