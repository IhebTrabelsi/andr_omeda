from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class MessageAutoDeleteTimerChanged(models.Model):
    message_auto_delete_time = models.IntegerField(_("message_auto_delete_time"),
                                                   blank=False)
