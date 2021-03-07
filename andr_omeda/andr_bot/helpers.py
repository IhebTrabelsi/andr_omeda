import requests
from django.conf import settings
from urllib.parse import urljoin


def set_webhook(cls, id):
    webhook = cls.objects.get(id=id)
    if not getattr(webhook, 'url'):

        webhook.error_during_creating = "ERROR: couldn't find url."
        webhook.save()
        return webhook
    else:
        # TODO [IHEB] needs to be changed later, this is only for testing
        url = getattr(obj, 'url')
        params = {'url': url}
        res = bot_api_request(method_name='setWebhook', params=params)
        return webhook


def bot_api_request(method_name='', params={}):
    return bot_api_request_for_bot_with_token(
        method_name=method_name,
        params=params,
        token=setting.BOT_TOKEN
    )


def bot_api_request_for_bot_with_token(token, method_name='', params={}):
    req_url = urljoin(
        settings.BOT_API_BASE_URL + token + '/',
        method_name
    )
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


def bot_with_token_exists(bot_token):
    res = bot_api_request_for_bot_with_token(method_name='getMe', token=bot_token)
    return "ok" in res and res["ok"] == True and res["result"]["is_bot"] == True


def get_bot_name_for_bot_token(bot_token):
    if bot_with_token_exists(bot_token=bot_token):
        res = bot_api_request_for_bot_with_token(method_name='getMe', token=bot_token)
        if not "ok" in res or res["ok"] == False:
            raise Exception("could not get bot name for some f*** reason.")
        return res["result"]["first_name"]
