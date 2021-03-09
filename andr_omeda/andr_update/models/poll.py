from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, Update


class Poll(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="poll",
        blank=True
    )
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="poll",
        blank=True
    )
    _id = models.CharField(_("_id"), blank=False)
    question = models.CharField(_("_id"), max_length=300, blank=False)
    total_voter_count = models.IntegerField(_("total_voter_count"), blank=False)
    is_closed = models.BooleanField(_("is_closed"), blank=False)
    is_anonymous = models.BooleanField(_("is_anonymous"), blank=False)
    type = models.CharField(_("type"), blank=False)
    allows_multiple_answers = models.BooleanField(_("allows_multiple_answers"), blank=False)
    correct_option_id = models.IntegerField(_("correct_option_id"), blank=True)
    explanation = models.CharField(_("explanation"), max_length=100, blank=True)
    open_period = models.IntegerField(_("open_period"), blank=True)
    close_date = models.IntegerField(_("close_date"), blank=True)
