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
    type = models.CharField(_("type"), blank=False)
    data = models.CharField(_("data"), blank=True)
    phone_number = models.CharField(_("phone_number"), blank=True)
    email = models.CharField(_("email"), blank=True)
    hash = models.CharField(_("hash"), blank=False)
