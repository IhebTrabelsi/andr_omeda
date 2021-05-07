from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from andr_omeda.andr_bot.helpers import bot_with_token_exists, \
    get_bot_name_for_bot_token
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from andr_omeda.andr_bot.tasks import async_set_webhook


class BotERPOwner(models.Model):
    owner_erp_name = models.CharField(_('owner-erp-name'), max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def owner_with_name_exists(cls, user_erp_name):
        qs = cls.objects.filter(owner_erp_name=user_erp_name)
        if not qs.exists():
            raise ValidationError({'user_erp_name': 'Name of user not registered as ERP user.'})

    @classmethod
    def get_bot_with_token_for_user_with_name(cls, name, **ser_data):
        token_owner = cls.objects.get(
            owner_erp_name=name,
            bots__token=ser_data['token']
        )

        return token_owner.bots.get()


class Bot(models.Model):
    token = models.CharField(_('bot-token'), max_length=50, unique=True)
    allowed_update_types = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=None,
    )
    erp_owner = models.ForeignKey(
        "BotERPOwner",
        on_delete=models.CASCADE,
        related_name='bots',
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # async_set_webhook.delay(self.token)
        super().save(*args, **kwargs)
