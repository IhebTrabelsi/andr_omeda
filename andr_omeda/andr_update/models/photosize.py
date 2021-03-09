from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, \
    Animation, Audio, Document, Sticker, Video, \
    VideoNote, Game
"""


class PhotoSize(models.Model):
    animation = models.OneToOneField(
        "Animation",
        on_delete=models.CASCADE,
        related_name="thumb",
        blank=True
    )
    audio = models.OneToOneField(
        "Audio",
        on_delete=models.CASCADE,
        related_name="thumb",
        blank=True
    )
    document = models.OneToOneField(
        "Document",
        on_delete=models.CASCADE,
        related_name="thumb",
        blank=True
    )
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="photo",
        blank=True
    )
    sticker = models.OneToOneField(
        "Sticker",
        on_delete=models.CASCADE,
        related_name="thumb",
        blank=True
    )
    video = models.OneToOneField(
        "Video",
        on_delete=models.CASCADE,
        related_name="thumb",
        blank=True
    )
    video_note = models.OneToOneField(
        "VideoNote",
        on_delete=models.CASCADE,
        related_name="thumb",
        blank=True
    )
    game = models.ForeignKey(
        "Game",
        on_delete=models.CASCADE,
        related_name="photo",
        blank=True
    )
    chat_photo_message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="new_chat_photo",
        blank=True
    )

    file_id = models.TextField(_("file_id"), blank=False)
    file_unique_id = models.TextField(_("file_unique_id"), blank=False)
    width = models.IntegerField(_("width"), blank=False)
    height = models.IntegerField(_("height"), blank=False)
    file_size = models.IntegerField(_("file_size"), blank=True)
