from django.db import models
from django.utils.translation import ugettext_lazy as _


class VoiceChatEnded(models.Model):
    message = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="voice_chat_ended",
        blank=True
    )
    duration = models.IntegerField(_("duration"), blank=False)
