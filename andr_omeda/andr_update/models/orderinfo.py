from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, SuccessfulPayment, \
    PreCheckoutQuery
"""


class OrderInfo(models.Model):
    successful_paayment = models.OneToOneField(
        "SuccessfulPayment",
        on_delete=models.CASCADE,
        related_name="order_info",
        blank=True
    )
    name = models.TextField(_("name"), blank=False)
    phone_number = models.TextField(_("phone_number"), blank=False)
    email = models.TextField(_("email"), blank=False)
