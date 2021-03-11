from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Update(models.Model):
    andr_id = models.OneToOneField(
        "Andrid",
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name="update"
    )
