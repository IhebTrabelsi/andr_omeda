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


@shared_task
def async_set_webhook(bot) -> None:
    if settings.DEBUG:
        webhook_base_url = settings.WEBHOOK_URL + "/webhooks/update/" + bot.token + "/"
    else:
        webhook_base_url = settings.SCALEHERO_DOMAIN + "/webhooks/update/" + bot.token + "/"
    print("///////////////////////////////////////////////")
    print(webhook_base_url)
    if not bot_with_token_exists(bot.token):
        raise TelegramBotDoesNotExist(bot.token)
    print("----------------------------------------")

    allowed_update_types_param = config_bot_with_update_types()
    res = bot_api_request_for_bot_with_token(
        bot.token,
        settings.SET_WEBHOOK_FUNCTION_NAME,
        {'url': webhook_base_url,
            'allowed_updates': allowed_update_types_param}
    )
    print(res)

    time.sleep(60 * 3)
    # save bot to database
    if res['ok'] == True:
        bot.save()
    else:
        raise TelegramBotWebhookSetError(bot.token)


def create_bot_async(obj, *args, **kwargs):
    obj_token = getattr(obj, 'token', 'undefined')
    if obj_token == 'undefined':
        raise TelegramBotAsyncCreationFieldError(obj_token)
    if obj.id:
        raise TelegramBotAsyncCreationError(obj_token)
    async_set_webhook.delay(obj)