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
    title = models.TextField(_("title"), blank=False)
    address = models.TextField(_("address"), blank=False)
    foursquare_id = models.TextField(_("foursquare_id"), blank=True)
    foursquare_type = models.TextField(_("foursquare_type"), blank=True)
    google_place_id = models.TextField(_("google_place_id"), blank=True)
    google_place_type = models.TextField(_("google_place_type"), blank=True)
