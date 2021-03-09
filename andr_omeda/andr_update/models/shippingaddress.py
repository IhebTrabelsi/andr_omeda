from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, OrderInfo, ShippingQuery
"""


class ShippingAddress(models.Model):
    order_info = models.OneToOneField(
        "OrderInfo",
        on_delete=models.CASCADE,
        related_name="shipping_address",
        blank=True
    )
    shipping_query = models.OneToOneField(
        "ShippingQuery",
        on_delete=models.CASCADE,
        related_name="shipping_address",
        blank=False
    )
    country_code = models.TextField(_("country_code"), blank=False)
    state = models.TextField(_("state"), blank=False)
    city = models.TextField(_("city"), blank=False)
    street_line1 = models.TextField(_("street_line1"), blank=False)
    street_line2 = models.TextField(_("street_line2"), blank=False)
    post_code = models.TextField(_("post_code"), blank=False)
