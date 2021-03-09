from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Contact(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="contact",
        blank=True
    )
    phone_number = models.TextField(_("phone_number"), blank=False)
    first_name = models.TextField(_("first_name"), blank=False)
    last_name = models.TextField(_("last_name"), blank=True)
    user_id = models.IntegerField(_("user_id"), blank=True)
    vcard = models.TextField(_("vcard"), blank=True)
