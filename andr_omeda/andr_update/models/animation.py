from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, Game
"""


class Animation(models.Model):
    message = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="animation",
        blank=True
    )
    game = models.OneToOneField(
        "Game",
        on_delete=models.CASCADE,
        related_name="animation",
        blank=True
    )
    file_id = models.TextField(_("file_id"), blank=False)
    file_unique_id = models.TextField(_("file_unique_id"), blank=False)
    width = models.IntegerField(_("width"), blank=False)
    height = models.IntegerField(_("height"), blank=False)
    duration = models.IntegerField(_("duration"), blank=False)
    file_name = models.TextField(_("file_name"), blank=True)
    mime_type = models.TextField(_("mime_type"), blank=True)
    file_size = models.IntegerField(_("file_size"), blank=True)
