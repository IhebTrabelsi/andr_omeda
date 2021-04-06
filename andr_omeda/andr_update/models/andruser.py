from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, ProximityAlertTriggered, \
    InlineQuery, ChosenInlineResult, CallbackQuery, ShippingQuery, \
    PreCheckoutQuery
"""


class Andruser(models.Model):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="message_from",
        blank=True,
        null=True
    )
    bot_sender = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="via_bot",
        blank=True,
        null=True
    )
    user_members_message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="new_user_members",
        blank=True,
        null=True
    )
    user_leaving_member_message = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="left_user_member",
        blank=True,
        null=True
    )
    inline_query = models.OneToOneField(
        "InlineQuery",
        on_delete=models.CASCADE,
        related_name="inline_query_from",
        blank=True,
        null=True
    )
    callback_query = models.OneToOneField(
        "CallbackQuery",
        on_delete=models.CASCADE,
        related_name="callback_query_from",
        blank=True,
        null=True
    )


    user_id = models.BigIntegerField(_("user_id"), blank=False, primary_key=True)
    is_bot = models.BooleanField(_("is_bot"), blank=False)
    first_name = models.TextField(_("first_name"), blank=False)
    last_name = models.TextField(_("last_name"), blank=True)
    username = models.TextField(_("username"), blank=True)
    language_code = models.TextField(_("language_code"), blank=True)
    can_join_groups = models.BooleanField(_("can_join_groups"), blank=True, null=True)
    can_read_all_group_messages = models.BooleanField(_("can_read_all_group_messages"), blank=True, null=True)
    supports_inline_queries = models.BooleanField(_("supports_inline_queries"), blank=True, null=True)

    @classmethod
    def get_user_with_id_and_first_name(cls, user_id, first_name):
        try:
            obj = Person.objects.get(user_id=user_id, first_name=first_name)
            return obj
        except cls.DoesNotExist:
            raise cls.DoesNotExist

    @classmethod
    def user_with_id_exists(cls, user_id):
        return cls.objects.filter(user_id=user_id).exists()

    @classmethod
    def get_user_with_id(cls, user_id):
        if cls.user_with_id_exists(user_id):
            return cls.objects.get(user_id=user_id)

    def __str__(self):
        return "User with id:%i" % self.user_id

    @classmethod
    def context_user_unicity_check_for_field_and_context(cls, data, field='', context=None, prefix=''):
        if not context:
            raise Exception("context not provided")
        if not data.get(field, None):
            return context
        _id = data[field].get('user_id', None)
        if not _id:
            raise Exception("KeyError something wrong with user_id")
        user = cls.get_user_with_id(user_id=_id)
        if user:
            data.pop(field)
            #data[field] = {'chat_id': 1000000000, 'first_name': 'Iheb', 'last_name': 'Ben Said', 'type': 'private'}
            context['validated_data'] = data
            context['unicity'][prefix + '__' + field] = user.user_id
        else:
            pass
        
        return context 
