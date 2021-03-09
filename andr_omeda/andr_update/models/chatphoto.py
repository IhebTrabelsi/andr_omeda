from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Chat


class ChatPhoto(models.Model):
    small_file_id = models.TextField(_("small_file_id"), blank=False)
    small_file_unique_id = models.TextField(_("small_file_unique_id"), blank=False)
    big_file_id = models.TextField(_("big_file_id"), blank=False)
    big_file_unique_id = models.TextField(_("big_file_unique_id"), blank=False)
    chat = models.OneToOneField(
        Chat,
        on_delete=models.CASCADE,
        related_name="photo",
        blank=True
    )
