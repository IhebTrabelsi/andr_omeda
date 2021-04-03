from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Andrid


class Update(models.Model):
    update_id = models.OneToOneField(
        Andrid,
        on_delete=models.RESTRICT,
        related_name="update",
        blank=False,
        null=True
    )
    message = models.ForeignKey(
        "Message",
        on_delete=models.RESTRICT,
        related_name="update",
        blank=False,
        null=True
    )
    edited_message = models.ForeignKey(
        "Message",
        on_delete=models.RESTRICT,
        related_name="update_for_this_edited_message",
        blank=False,
        null=True
    )
    channel_post = models.ForeignKey(
        "Message",
        on_delete=models.RESTRICT,
        related_name="update_for_this_channel_post",
        blank=False,
        null=True
    )
    edited_channel_post = models.ForeignKey(
        "Message",
        on_delete=models.RESTRICT,
        related_name="update_for_this_edited_channel_post",
        blank=False,
        null=True
    )


    def __str__(self):
        if self.id:
            return "Update with pgId: %i" % self.id
