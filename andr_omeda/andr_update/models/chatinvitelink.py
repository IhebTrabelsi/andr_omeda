from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChatInviteLink(models.Model):
    invite_link = models.TextField(_("invite_link"), blank=False)
    creator = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        blank=True,
    )
    chat_member_update = models.OneToOneField(
        "ChatMemberUpdated",
        on_delete=models.RESTRICT,
        related_name="invite_link",
        blank=True,
        null=True
    )
    is_primary = models.BooleanField(_("is_primary"), blank=False)
    is_revoked = models.BooleanField(_("is_revoked"), blank=False)
    expire_date = models.IntegerField(_("expire_date"), blank=True)
    member_limit = models.IntegerField(_("member_limit"), blank=True)
