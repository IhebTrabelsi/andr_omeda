from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, ChatLocation, Venue


class Location(models.Model):
    chat_location = models.OneToOneField(
        ChatLocation,
        on_delete=models.CASCADE,
        related_name="location",
        blank=True
    )
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="location",
        blank=True
    )
    venue = models.OneToOneField(
        Venue,
        on_delete=models.CASCADE,
        related_name="location",
        blank=True
    )
    longitude = models.FloatField(_("longitude"), blank=False)
    latitude = models.FloatField(_("latitude"), blank=False)
    horizontal_accuracy = models.FloatField(_("horizontal_accuracy"), blank=True)
    live_period = models.IntegerField(_("live_period"), blank=True)
    heading = models.IntegerField(_("heading"), blank=True)
    proximity_alert_radius = models.IntegerField(_("proximity_alert_radius"), blank=True)