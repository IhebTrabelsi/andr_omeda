from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, Game
"""


class MessageEntity(models.Model):
    user = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        related_name="mentions",
        blank=True,
        null=True
    )
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="entities",
        blank=True,
        null=True
    )
    message_captioned = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="caption_entities",
        blank=True,
        null=True
    )
    game = models.ForeignKey(
        "Game",
        on_delete=models.CASCADE,
        related_name="text_entities",
        blank=True,
        null=True
    )
    poll = models.ForeignKey(
        "Poll",
        on_delete=models.CASCADE,
        related_name="explanation_entities",
        blank=True,
        null=True
    )
    type = models.TextField(_("type"), blank=False)
    offset = models.IntegerField(_("offset"), blank=False)
    length = models.IntegerField(_("length"), blank=False)
    url = models.TextField(_("url"), blank=True)
    language = models.TextField(_("language"), blank=True)

    def __str__(self):
        return "MessageEntity %s"%self.type

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        return self

