from django.db.models.signals import post_save
from django.dispatch import receiver
from andr_omeda.andr_bot.models.bot import Bot
from andr_omeda.andr_bot.tasks import async_set_webhook
