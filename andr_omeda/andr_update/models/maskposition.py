from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Sticker


class MaskPosition(models.Model):
    sticker = models.OneToOneField(
        Sticker,
        on_delete=models.CASCADE,
        related_name="mask_position",
        blank=True
    )
    point = models.CharField(_("point"), blank=False)
    x_shift = models.FloatField(_("x_shift"), blank=False)
    y_shift = models.FloatField(_("y_shift"), blank=False)
    scale = models.FloatField(_("scale"), blank=False)
