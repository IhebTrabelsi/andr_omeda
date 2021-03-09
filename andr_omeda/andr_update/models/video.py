from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Video(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="video",
        blank=True
    )
    file_id = models.CharField(_("file_id"), blank=False)
    file_unique_id = models.CharField(_("file_unique_id"), blank=False)
    width = models.IntegerField(_("width"), blank=False)
    height = models.IntegerField(_("height"), blank=False)
    duration = models.IntegerField(_("duration"), blank=False)
    file_name = models.CharField(_("file_name"), blank=True)
    mime_type = models.CharField(_("mime_type"), blank=True)
    file_size = models.IntegerField(_("file_size"), blank=True)
