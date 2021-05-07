import requests
from django.conf import settings
from urllib.parse import urljoin
from andr_omeda.andr_bot.exceptions import TelegramBotDoesNotExist, \
    TelegramBotAsyncCreationError, TelegramBotAsyncCreationFieldError, \
    TelegramAPIResultParsingError


def bot_api_request_for_bot_with_token(token, method_name='', params={}):
    print("[bot_api_request_for_bot_with_token]")

    req_url = urljoin(
        settings.BOT_API_BASE_URL + token + "/",
        method_name
    )
    print(req_url)
    res = requests.post(req_url, data=params)
    return res.json()


def webhookinfo_for_bot_with_id(cls, id):
    bot = cls.objects.get(id=id)
    method_name = bot.get_webhookinfo_methodname()
    res = bot_api_request(method_name=method_name, params={})
    # TODO [IHEB] place holder for later to come API ENCAPS OBJECT
    if not res["ok"] == True:
        raise Exception("Failing bot api request")
    try:
        url = res["result"]["url"]

    except:
        raise Exception("request succeded but can't access result. ")


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
