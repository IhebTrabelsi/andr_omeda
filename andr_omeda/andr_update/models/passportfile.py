from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, EncryptedPassportElement


class PassportFile(models.Model):
    encrypted_passport_element = models.ForeignKey(
        EncryptedPassportElement,
        on_delete=models.CASCADE,
        related_name="files",
        blank=True
    )
    encrypted_passport_element_front = models.OneToOneField(
        EncryptedPassportElement,
        on_delete=models.CASCADE,
        related_name="front_side",
        blank=True
    )
    encrypted_passport_element_reverse = models.OneToOneField(
        EncryptedPassportElement,
        on_delete=models.CASCADE,
        related_name="reverse_side",
        blank=True
    )
    encrypted_passport_element_selfie = models.OneToOneField(
        EncryptedPassportElement,
        on_delete=models.CASCADE,
        related_name="selfie",
        blank=True
    )
    encrypted_passport_element_translation = models.ForeignKey(
        EncryptedPassportElement,
        on_delete=models.CASCADE,
        related_name="translation",
        blank=True
    )
