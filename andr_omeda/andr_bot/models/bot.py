from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from andr_omeda.andr_bot.exceptions import TelegramBotFieldAccessError
from andr_omeda.andr_moderation.models import ModeratedObject


class Bot(models.Model):
    token = models.CharField(_('bot-token'), max_length=50, unique=True)
    allowed_update_types = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=None,
    )
    chats = models.ManyToManyField(
        "andr_update.Chat",
        related_name="bots",
        blank=True
    )
    is_webhook_set = models.BooleanField(_('is_webhook_set'), default=False)
    webhook_result_description = models.CharField(
        _('webhook_error_description'),
        blank=True,
        default='',
        max_length=300
    )
    erp_owner = models.ForeignKey(
        "BotERPOwner",
        on_delete=models.CASCADE,
        related_name='bots',
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def count_pending_moderated_objects(self):
        query = Q(chats__moderated_objects=ModeratedObject.STATUS_PENDING)
        query.add(Q(id=self.id), Q.AND)
        return Bot.objects.filter(query).count()
