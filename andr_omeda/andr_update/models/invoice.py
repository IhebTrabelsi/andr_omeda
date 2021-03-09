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
    title = models.TextField(_("title"), blank=False)
    description = models.TextField(_("description"), blank=False)
    start_parameter = models.TextField(_("start_parameter"), blank=False)
    currency = models.TextField(_("currency"), blank=False)
    total_amount = models.IntegerField(_("total_amount"), blank=False)
