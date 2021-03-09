from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, OrderInfo


class ShippingAddress(models.Model):
    order_info = models.OneToOneField(
        OrderInfo,
        on_delete=models.CASCADE,
        related_name="shipping_address",
        blank=True
    )
    country_code = models.CharField(_("country_code"), blank=False)
    state = models.CharField(_("state"), blank=False)
    city = models.CharField(_("city"), blank=False)
    street_line1 = models.CharField(_("street_line1"), blank=False)
    street_line2 = models.CharField(_("street_line2"), blank=False)
    post_code = models.CharField(_("post_code"), blank=False)
