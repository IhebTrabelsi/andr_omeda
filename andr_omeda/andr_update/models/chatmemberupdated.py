from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChatMemberUpdated(models.Model):
    chat = models.OneToOneField(
        "Chat",
        on_delete=models.CASCADE,
        blank=False
    )
    user = models.OneToOneField(
        "Andruser",
        on_delete=models.CASCADE,
        blank=False
    )
    update_for_my_chat_member = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        blank=False,
        related_name="my_chat_member"
    )
    update_for_chat_member = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        blank=False,
        related_name="chat_member"
    )
    invite_link = models.OneToOneField(
        "Update",
        on_delete=models.CASCADE,
        blank=True,
    )
    date = models.IntegerField(_("date"), blank=False)
