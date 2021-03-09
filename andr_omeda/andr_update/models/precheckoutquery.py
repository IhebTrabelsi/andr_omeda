from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class PreCheckoutQuery(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE
        related_name="pre_checkout_query"
        blank=True
    )
    id = models.CharField(_("id"), blank=False)
    total_amount = models.IntegerField(_("total_amount"), blank=False)
    currency = models.CharField(_("currency"), blank=False)
    invoice_payload = models.CharField(_("invoice_payload"), blank=False)
    shipping_option_id = models.CharField(_("shipping_option_id"), blank=True)
