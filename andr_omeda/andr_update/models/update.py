from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Andrid, Message


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

    @classmethod 
    def get_need_sanitize_attrs_rec(cls):
        return ['message', 'edited_message', 'channel_post', \
            'my_chat_member', ('my_chat_member', 'old_chat_member'), \
            ('my_chat_member', 'new_chat_member')]
    
    @classmethod
    def get_need_sanitize_attrs(cls):
        attrs_list = cls.get_need_sanitize_attrs_rec()
        for m in attrs_list[:3]:
            attrs_list.append((m, 'reply_to_message'))
            attrs_list.append((m, 'pinned_message'))
        return attrs_list

    """def save(self, *args, **kwargs):
        if self.edited_message:
            message_to_edit = Message.get_message_for_message_id_and_chat_id(
                message_id=self.edited_message.message_id,
                chat_id=self.edited_message.chat.chat_id
                )
            message_to_edit.edit_date = self.edited_message.edit_date
            message_to_edit.text = self.edited_message.text 
            message_to_edit.save()
        super().save(*args, **kwargs) """
