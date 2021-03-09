from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, Game


class MessageEntity(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="entities",
        blank=True
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="caption_entities",
        blank=True
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="text_entities",
        blank=True
    )
    poll = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="explanation_entities",
        blank=True
    )
    type = models.CharField(_("type"), blank=False)
    offset = models.IntegerField(_("offset"), blank=False)
    length = models.IntegerField(_("length"), blank=False)
    url = models.CharField(_("url"), blank=True)
    language = models.CharField(_("language"), blank=True)
