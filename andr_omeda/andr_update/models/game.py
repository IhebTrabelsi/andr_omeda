from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Game(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="contact",
        blank=True
    )
    title = models.CharField(_("title"), blank=False)
    description = models.CharField(_("description"), blank=False)
    text = models.CharField(_("text"), max_length=4096, blank=True)
