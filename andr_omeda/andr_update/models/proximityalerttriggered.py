from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message


class ProximityAlertTriggered(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="proximity_alert_triggered",
        blank=True
    )
    traveler = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        related_name="traveler_proximity_alert_triggered_set",
        blank=False
    )
    watcher = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        related_name="watcher_proximity_alert_triggered_set",
        blank=False
    )
    distance = models.IntegerField(_("distance"), blank=False)
