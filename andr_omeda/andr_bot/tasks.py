from celery import shared_task
import requests
from django.conf import settings
from andr_omeda.andr_bot.helpers import bot_api_request_for_bot_with_token, \
    bot_with_token_exists, config_bot_with_update_types
from andr_omeda.andr_bot.exceptions import TelegramBotDoesNotExist, TBDE, \
    TelegramBotWebhookSetError

# TODO check if bot exists in telegram before setwebhook !
# act accordinly wheen bot doesn't exist / setwebhook fails

# TODO consider registering bot basic info between checking existeence of
# bot and saving it (maybe done after saving as it's on separate async task)
import time
from django.db import transaction
from andr_omeda.andr_bot.models.bot import Bot
from andr_omeda.andr_bot.helpers import parse_setwebhook_res


@shared_task
def async_set_webhook(token) -> None:
    with transaction.atomic():
        if settings.DEBUG:
            webhook_base_url = settings.WEBHOOK_URL + "/webhooks/update/" + token + "/"
        else:
            webhook_base_url = settings.SCALEHERO_DOMAIN + "/webhooks/update/" + token + "/"
        print("///////////////////////////////////////////////")
        print(webhook_base_url)
        if not bot_with_token_exists(token):
            raise TelegramBotDoesNotExist(token)
        print("----------------------------------------")

        allowed_update_types_param = config_bot_with_update_types()
        res = bot_api_request_for_bot_with_token(
            token,
            settings.SET_WEBHOOK_FUNCTION_NAME,
            {'url': webhook_base_url,
                'allowed_updates': allowed_update_types_param}
        )
        time.sleep(60 * 3)
        bot = Bot.objects.get(token=token)
        res_ok, res_description = parse_setwebhook_res(res)
        bot.is_webhook_set = res_ok
        bot.webhook_result_description = res_description
        bot.save()
