from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class PreCheckoutQuery(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="pre_checkout_query",
        blank=True
    )
    pre_checkout_query_id = models.TextField(_("pre_checkout_query_id"), blank=False)
    total_amount = models.IntegerField(_("total_amount"), blank=False)
    currency = models.TextField(_("currency"), blank=False)
    invoice_payload = models.TextField(_("invoice_payload"), blank=False)
    shipping_option_id = models.TextField(_("shipping_option_id"), blank=True)
