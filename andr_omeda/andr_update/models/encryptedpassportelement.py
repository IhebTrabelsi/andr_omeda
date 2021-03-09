from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, PassportData


class EncryptedPassportElement(models.Model):
    passport_data = models.ForeignKey(
        PassportData,
        on_delete=models.CASCADE,
        related_name="data",
        blank=True
    )
    type = models.TextField(_("type"), blank=False)
    data = models.TextField(_("data"), blank=True)
    phone_number = models.TextField(_("phone_number"), blank=True)
    email = models.TextField(_("email"), blank=True)
    hash = models.TextField(_("hash"), blank=False)
