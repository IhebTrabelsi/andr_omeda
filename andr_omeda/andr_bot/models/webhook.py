# model that keeps track of all current and previous
# webhooks used.
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_bot.models import Bot


class WebHook(models.Model):
    url = models.URLField(_('url'), blank=False, null=False)
    created = models.DateTimeField(editable=False, null=False, blank=False, auto_now_add=True)
    error_during_creating = models.CharField(_('error'), max_length=255, blank=True, default='')
    bot = models.OneToOneField(
        Bot,
        on_delete=models.SET_NULL,
        null=True,
        related_name="webhook"
    )

    class Meta:
        unique_together = ('bot',)

    @classmethod
    def create_webhook(cls, url):
        # TODO [IHEB] placeholder until bot api created
        bot = Bot.create_bot(settings.BOT_TOKEN)
        if bot == None:
            raise Exception("could not create webhook, bot doesn't exist in telegram")
        webhook, created = cls.objects.get_or_create(
            bot=bot,
            defaults={'url': url, },
        )
