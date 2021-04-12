from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Update


class ChatMember(models.Model):
    """
    This object contains information about one member of a chat.
    """
    old_member = models.ForeignKey(
        "ChatMemberUpdated",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        related_name="old_chat_member"
    )
    new_member = models.ForeignKey(
        "ChatMemberUpdated",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        related_name="new_chat_member"
    )
    user = models.ForeignKey(
        "Andruser",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    status = models.CharField(_("status"), max_length=255, blank=False)
    custom_title = models.CharField(_("status"), max_length=255, blank=True)
    is_anonymous = models.BooleanField(_("is_anonymous"), blank=True, null=True)
    can_be_edited = models.BooleanField(_("can_be_edited"), blank=True, null=True)
    can_manage_chat = models.BooleanField(_("can_manage_chat"), blank=True, null=True)
    can_post_messages = models.BooleanField(_("can_post_messages"), blank=True, null=True)
    can_edit_messages = models.BooleanField(_("can_edit_messages"), blank=True, null=True)
    can_delete_messages = models.BooleanField(_("can_delete_messages"), blank=True, null=True)
    can_manage_voice_chats = models.BooleanField(_("can_manage_voice_chats"), blank=True, null=True)
    can_restrict_members = models.BooleanField(_("can_restrict_members"), blank=True, null=True)
    can_promote_members = models.BooleanField(_("can_promote_members"), blank=True, null=True)
    can_change_info = models.BooleanField(_("can_change_info"), blank=True, null=True)
    can_invite_users = models.BooleanField(_("can_invite_users"), blank=True, null=True)
    can_pin_messages = models.BooleanField(_("can_pin_messages"), blank=True, null=True)
    is_member = models.BooleanField(_("is_member"), blank=True, null=True)
    can_send_messages = models.BooleanField(_("can_send_messages"), blank=True, null=True)
    can_send_media_messages = models.BooleanField(_("can_send_media_messages"), blank=True, null=True)
    can_send_polls = models.BooleanField(_("can_send_polls"), blank=True, null=True)
    can_send_other_messages = models.BooleanField(_("can_send_other_messages"), blank=True, null=True)
    can_add_web_page_previews = models.BooleanField(_("can_add_web_page_previews"), blank=True, null=True)
    until_date = models.IntegerField(_("until_date"), blank=True, null=True)

   