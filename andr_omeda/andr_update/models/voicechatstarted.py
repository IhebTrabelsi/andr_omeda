from django.db import models
from django.utils.translation import ugettext_lazy as _


class VoiceChatStarted(models.Model):
    message = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="voice_chat_started",
        blank=True
    )
