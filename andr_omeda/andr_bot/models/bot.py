from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from andr_omeda.andr_bot.helpers import bot_with_token_exists, \
    get_bot_name_for_bot_token
from django.utils import timezone


class Bot(models.Model):
    name = models.CharField(_('name'), max_length=255, blank=False, null=True)
    is_webhook_active = models.BooleanField(_('is_active'), default=False)
    created = models.DateTimeField(editable=False, null=False, blank=False, auto_now_add=True)
    token = models.CharField(
        _('token'),
        max_length=46,
        default=settings.BOT_TOKEN,
        primary_key=True
    )

    class Meta:
        unique_together = ('name', 'token',)

    def get_webhookinfo_methodname():
        # TODO [IHEB] place holder for later to come API ENCAPS OBJECT
        return 'getWebhookInfo'

    @classmethod
    def create_bot(cls, bot_token):
        if bot_with_token_exists(bot_token=bot_token):
            bot, created = cls.objects.get_or_create(
                token=bot_token,
                defaults={'name': get_bot_name_for_bot_token(bot_token=bot_token)},
            )
            return bot
        return None
