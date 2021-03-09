from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class SuccessfulPayment(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="successful_payment",
        blank=True
    )
    currency = models.CharField(_("currency"), blank=False)
    total_amount = models.IntegerField(_("total_amount"), blank=False)
    invoice_payload = models.CharField(_("invoice_payload"), blank=False)
    shipping_option_id = models.CharField(_("invoice_payload"), blank=True)
    telegram_payment_charge_id = models.CharField(_("telegram_payment_charge_id"), blank=False)
    provider_payment_charge_id = models.CharField(_("provider_payment_charge_id"), blank=False)
