from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class Venue(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="venue",
        blank=True
    )
    title = models.CharField(_("title"), blank=False)
    address = models.CharField(_("address"), blank=False)
    foursquare_id = models.CharField(_("foursquare_id"), blank=True)
    foursquare_type = models.CharField(_("foursquare_type"), blank=True)
    google_place_id = models.CharField(_("google_place_id"), blank=True)
    google_place_type = models.CharField(_("google_place_type"), blank=True)
