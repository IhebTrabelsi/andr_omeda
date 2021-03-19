from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update
from django.contrib.postgres.fields import JSONField


class PollAnswer(models.Model):
    option_ids = models.JSONField(_("option_ids"), blank=False)
    poll_id = models.TextField(_("poll_id"), blank=False)
