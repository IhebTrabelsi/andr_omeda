from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Invoice(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="invoice",
        blank=True
    )
    title = models.CharField(_("title"), blank=False)
    description = models.CharField(_("description"), blank=False)
    start_parameter = models.CharField(_("start_parameter"), blank=False)
    currency = models.CharField(_("currency"), blank=False)
    total_amount = models.IntegerField(_("total_amount"), blank=False)
