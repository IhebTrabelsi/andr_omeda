from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Andrid


class Update(models.Model):
    update_id = models.OneToOneField(
        Andrid,
        on_delete=models.RESTRICT,
        related_name="update",
        blank=False,
        null=True
    )
