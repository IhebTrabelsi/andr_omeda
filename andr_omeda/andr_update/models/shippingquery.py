from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ShippingQuery(models.Model):
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="shipping_query",
        blank=True
    )
    shipping_query_id = models.TextField(_("id"), blank=False)
    invoice_payload = models.TextField(_("invoice_payload"), blank=False)
