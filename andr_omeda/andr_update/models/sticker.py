from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Sticker(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="sticker",
        blank=True,
        null=True
    )
    file_id = models.TextField(_("file_id"), blank=False)
    file_unique_id = models.TextField(_("file_unique_id"), blank=False)
    width = models.IntegerField(_("width"), blank=False)
    height = models.IntegerField(_("height"), blank=False)
    is_animated = models.BooleanField(_("is_animated"), blank=False)
    emoji = models.TextField(_("emoji"), blank=True)
    set_name = models.TextField(_("set_name"), blank=True)

    file_size = models.IntegerField(_("file_size"), blank=True, null=True)

    def __str__(self):
        if self.id:
            return "Sticker with pgId: %i" % self.id
