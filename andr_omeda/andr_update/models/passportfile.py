from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, EncryptedPassportElement


class PassportFile(models.Model):
    encrypted_passport_element = models.ManyToManyField(
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
    encrypted_passport_element_translation = models.ManyToManyField(
        EncryptedPassportElement,
        on_delete=models.CASCADE,
        related_name="translation",
        blank=True
    )
    file_id = models.TextField(_("file_id"), blank=False)
    file_unique_id = models.TextField(_("file_id"), blank=False, primary_key=True)
    file_size = models.IntegerField(_("file_size"), blank=False)
    file_date = models.IntegerField(_("file_date"), blank=False)

    @classmethod
    def bulk_passportfile_or_instance(cls, data):
        bulk = []
        for item in data:
            unique_id = item.get('file_unique_id')
            if cls.passportfile_with_unique_id_exists(unique_id=unique_id):
                bulk.append(cls.objects.get(pk=unique_id))
            else:
                bulk.append(cls.objects.create(**item))
        return bulk

    @classmethod
    def passportfile_with_unique_id_exists(cls, unique_id):
        return cls.objects.filter(file_unique_id=unique_id).exists()
