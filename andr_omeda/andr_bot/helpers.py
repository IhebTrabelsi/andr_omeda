import requests
from django.conf import settings
from django.db import transaction
from urllib.parse import urljoin
from andr_omeda.andr_bot.exceptions import TelegramBotDoesNotExist, \
    TelegramBotAsyncCreationError, TelegramBotAsyncCreationFieldError, \
    TelegramAPIResultParsingError
from andr_omeda.andr_bot.models.bot import Bot


def bot_api_request_for_bot_with_token(token, method_name='', params={}):
    print("[bot_api_request_for_bot_with_token]")

    req_url = urljoin(
        settings.BOT_API_BASE_URL + token + "/",
        method_name
    )
    print(req_url)
    res = requests.post(req_url, data=params)
    return res.json()


def bot_with_token_exists(token):
    print("[bot_with_token_exists]")

    res = bot_api_request_for_bot_with_token(method_name='getMe', token=token)
    return "ok" in res and res["ok"] == True and res["result"]["is_bot"] == True


def bot_with_token_exists_and_res(token):
    print("[bot_with_token_exists_and_res]")

    res = bot_api_request_for_bot_with_token(method_name='getMe', token=token)
    return "ok" in res and res["ok"] == True and res["result"]["is_bot"] == True, res


def parse_setwebhook_res(res):
    try:
        res_ok = res['ok']
        res_description = res['description']
    except Exception as e:
        raise TelegramAPIResultParsingError('setwebhook')
    return res_ok, res_description


def bot_basic_info(token):
    exist, res = bot_with_token_exists(token)
    if exist:
        return res
    else:
        raise TelegramBotDoesNotExist(token)


def get_bot_name_for_bot_token(bot_token):
    if bot_with_token_exists(bot_token=bot_token):
        res = bot_api_request_for_bot_with_token(method_name='getMe', token=bot_token)
        if not "ok" in res or res["ok"] == False:
            raise Exception("could not get bot name for some f*** reason.")
        return res["result"]["first_name"]


def config_bot_with_update_types(default=True, obj=None):
    if default or not obj:
        return settings.BOT_CONFIG_PARAM_ALLOWED_UPDATES

    return obj.allowed_update_types


def resolve_webhook_base_url(domain="", token=None):
    if not token:
        raise ValueError("[arg: token] need to be specified!")
    if settings.DEBUG:
        if domain == "":
            webhook_base_url = settings.WEBHOOK_URL + "/webhooks/update/" + token + "/"
        else:
            if domain.startswith("https://"):
                domain = domain[len("https://"):]
            elif domain.startswith("http://"):
                domain = domain[len("http://"):]

            webhook_base_url = settings.NGROK_PREFIX + domain + "/webhooks/update/" + token + "/"
    else:
        webhook_base_url = settings.SCALEHERO_DOMAIN + "/webhooks/update/" + token + "/"

    return webhook_base_url


def set_webhook_for_bot_with_token(domain="", token=None):
    try:
        webhook_base_url = resolve_webhook_base_url(domain=domain, token=token)

        if not bot_with_token_exists(token):
            raise TelegramBotDoesNotExist(token)

        allowed_update_types_param = config_bot_with_update_types()

        res = bot_api_request_for_bot_with_token(
            token,
            settings.SET_WEBHOOK_FUNCTION_NAME,
            {'url': webhook_base_url,
                'allowed_updates': allowed_update_types_param}
        )

        return res

    except ValueError as e:
        raise ValueError(e.message)


def update_webhook_fields_for_bot_with_token(token=None, request_res=None):
    if not token:
        raise ValueError("[arg: token] need to be specified!")
    if not request_res:
        raise ValueError("[arg: request_res] need to be specified!")

    with transaction.atomic():
        bot = Bot.objects.get(token=token)
        res_ok, res_description = parse_setwebhook_res(request_res)
        bot.is_webhook_set = res_ok
        bot.webhook_result_description = res_description
        bot.save()
