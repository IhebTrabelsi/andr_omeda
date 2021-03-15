from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChatInviteLink(models.Model):
    invite_link = models.TextField(_("invite_link"), blank=False)
    creator = models.OneToOneField(
        "Andruser",
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )
    is_primary = models.BooleanField(_("is_primary"), blank=False)
    is_revoked = models.BooleanField(_("is_revoked"), blank=False)
    expire_date = models.IntegerField(_("expire_date"), blank=True)
    member_limit = models.IntegerField(_("member_limit"), blank=True, max_length=99999)
