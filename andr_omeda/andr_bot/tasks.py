from celery import shared_task
import requests
from django.conf import settings
from andr_omeda.andr_bot.helpers import set_webhook_for_bot_with_token, \
    parse_setwebhook_res, update_webhook_fields_for_bot_with_token
from andr_omeda.andr_bot.exceptions import TelegramBotDoesNotExist, TBDE, \
    TelegramBotWebhookSetError


# TODO consider registering bot basic info between checking existeence of
# bot and saving it (maybe done after saving as it's on separate async task)
import time
from django.db import transaction
from andr_omeda.andr_bot.models.bot import Bot


@shared_task
def async_set_webhook(token) -> None:
    with transaction.atomic():
        res = set_webhook_for_bot_with_token(token=token)
        update_webhook_fields_for_bot_with_token(token=token, request_res=res)
