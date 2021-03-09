from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, PassportData


class EncryptedCredentials(models.Model):
    passport_data = models.OneToOneField(
        PassportData,
        on_delete=models.CASCADE,
        related_name="credentials",
        blank=True
    )
    data = models.TextField(_("data"), blank=False)
    hash = models.TextField(_("hash"), blank=False)
    secret = models.TextField(_("secret"), blank=False)
