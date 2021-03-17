from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
"""from andr_omeda.andr_update.models import Message, ProximityAlertTriggered, \
    InlineQuery, ChosenInlineResult, CallbackQuery, ShippingQuery, \
    PreCheckoutQuery
"""


class Andruser(models.Model):
    message = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="message_from",
        blank=True
    )
    forwarder = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="forward_from",
        blank=True
    )
    bot_sender = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="via_bot",
        blank=True
    )
    entity_mention = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="user",
        blank=True
    )
    user_members_message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="new_user_members",
        blank=True
    )
    user_leaving_member_message = models.OneToOneField(
        "Message",
        on_delete=models.CASCADE,
        related_name="left_user_member",
        blank=True
    )
    proximity_alert_for_traveler = models.OneToOneField(
        "ProximityAlertTriggered",
        on_delete=models.CASCADE,
        related_name="traveler",
        blank=False
    )
    proximity_alert_for_watcher = models.OneToOneField(
        "ProximityAlertTriggered",
        on_delete=models.CASCADE,
        related_name="watcher",
        blank=False
    )
    inline_query = models.OneToOneField(
        "InlineQuery",
        on_delete=models.CASCADE,
        related_name="inline_query_from",
        blank=False
    )
    chosen_inline_result = models.OneToOneField(
        "ChosenInlineResult",
        on_delete=models.CASCADE,
        related_name="chosen_inline_result_from",
        blank=False
    )
    callback_query = models.OneToOneField(
        "CallbackQuery",
        on_delete=models.CASCADE,
        related_name="callback_query_from",
        blank=False
    )
    shipping_query = models.OneToOneField(
        "ShippingQuery",
        on_delete=models.CASCADE,
        related_name="shipping_query_from",
        blank=False
    )
    pre_checkout_query = models.OneToOneField(
        "PreCheckoutQuery",
        on_delete=models.CASCADE,
        related_name="pre_checkout_query_from",
        blank=False
    )

    user_id = models.BigIntegerField(_("user_id"), blank=False, primary_key=True)
    is_bot = models.BooleanField(_("is_bot"), blank=False)
    first_name = models.TextField(_("first_name"), blank=False)
    last_name = models.TextField(_("last_name"), blank=True)
    username = models.TextField(_("username"), blank=True)
    language_code = models.TextField(_("language_code"), blank=True)
    can_join_groups = models.BooleanField(_("can_join_groups"), blank=True)
    can_read_all_group_messages = models.BooleanField(_("can_read_all_group_messages"), blank=True)
    supports_inline_queries = models.BooleanField(_("supports_inline_queries"), blank=True)

    @classmethod
    def get_user_with_id_and_first_name(cls, user_id, first_name):
        try:
            obj = Person.objects.get(user_id=user_id, first_name=first_name)
            return obj
        except cls.DoesNotExist:
            raise cls.DoesNotExist

    @classmethod
    def user_with_id_exists(cls, user_id):
        return cls.objects.filter(pk=user_id).exists()

    @classmethod
    def get_user_with_id(cls, user_id):
        if cls.user_with_id_exists(user_id)
        return cls.objects.get(pk=user_id)
