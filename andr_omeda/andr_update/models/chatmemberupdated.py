from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChatMemberUpdated(models.Model):
    chat = models.ForeignKey(
        "Chat",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    from_user = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        blank=True,
    )
    date = models.IntegerField(_("date"), blank=False)
    update = models.ForeignKey(
        "Update",
        on_delete=models.CASCADE,
        related_name="my_chat_member",
        blank=True,
        null=True
    )
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        return self

    