from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Document(models.Model):
    file_id = models.TextField(_("file_id"), blank=False)
    file_unique_id = models.TextField(_("file_unique_id"), blank=False)
    file_name = models.TextField(_("file_name"), blank=True)
    mime_type = models.TextField(_("mime_type"), blank=True)
    file_size = models.IntegerField(_("file_size"), blank=True, null=True)

