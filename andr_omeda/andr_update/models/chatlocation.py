from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Chat


class ChatLocation(models.Model):
    chat = models.OneToOneField(
        Chat,
        on_delete=models.CASCADE,
        related_name="location",
        blank=True
    )
    address = models.CharField(_("address"), max_length=64, blank=Flase)
