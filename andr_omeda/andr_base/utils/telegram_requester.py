import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from andr_omeda.andr_base.utils import logging
from andr_omeda.andr_base.utils import types

try:
    from requests.packages.urllib3 import fields
    format_header_param = fields.format_header_param
except ImportError:
    format_header_param = None

proxy = None
session = None

API_URL = None
READ_TIMEOUT = 9999
CONNECT_TIMEOUT = 3.5
RETRY_ON_ERROR = False
SESSION_TIME_TO_LIVE = None

logger = logging.logger


def _make_request(token, method_name, method='get', params=None, files=None):
    """
    Makes a request to the Telegram API.
    :param token: The bot's API token. (Created with @BotFather)
    :param method_name: Name of the API method to be called. (E.g. 'getUpdates')
    :param method: HTTP method to be used. Defaults to 'get'.
    :param params: Optional parameters. Should be a dictionary with key-value pairs.
    :param files: Optional files.
    :return: The result parsed to a JSON dictionary.
    """
    if API_URL:
        request_url = API_URL.format(token, method_name)
    else:
        request_url = "https://api.telegram.org/bot{0}/{1}".format(token, method_name)

    logger.debug("Request: method={0} url={1} params={2} files={3}".format(
        method, request_url, params, files).replace(token, token.split(':')[0] + ":{TOKEN}"))
    read_timeout = READ_TIMEOUT
    connect_timeout = CONNECT_TIMEOUT
    if files and format_header_param:
        fields.format_header_param = _no_encode(format_header_param)
    if params:
        if 'timeout' in params:
            read_timeout = params.pop('timeout') + 10
        if 'connect-timeout' in params:
            connect_timeout = params.pop('connect-timeout') + 10

    result = None

    # session is one-time use
    session = requests.sessions.Session()
    result = session.request(
        method, request_url, params=params, files=files,
        timeout=(connect_timeout, read_timeout), proxies=proxy)

    logger.debug("The server returned: '{0}'".format(result.text.encode('utf8')))

    json_result = _check_result(method_name, result)
    if json_result:
        return json_result['result']


def _no_encode(func):
    def wrapper(key, val):
        if key == 'filename':
            return u'{0}={1}'.format(key, val)
        else:
            return func(key, val)

    return wrapper


def _check_result(method_name, result):
    """
    Checks whether `result` is a valid API response.
    A result is considered invalid if:
        - The server returned an HTTP response code other than 200
        - The content of the result is invalid JSON.
        - The method call was unsuccessful (The JSON 'ok' field equals False)
    :raises ApiException: if one of the above listed cases is applicable
    :param method_name: The name of the method called
    :param result: The returned result of the method request
    :return: The result parsed to a JSON dictionary.
    """
    try:
        result_json = result.json()
    except:
        if result.status_code != 200:
            raise ApiHTTPException(method_name, result)
        else:
            raise ApiInvalidJSONException(method_name, result)
    else:
        if not result_json['ok']:
            raise ApiTelegramException(method_name, result, result_json)

        return result_json


def send_message(
        token, chat_id, text,
        disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
        parse_mode=None, disable_notification=None, timeout=None):
    """
    Use this method to send text messages. On success, the sent Message is returned.
    :param token:
    :param chat_id:
    :param text:
    :param disable_web_page_preview:
    :param reply_to_message_id:
    :param reply_markup:
    :param parse_mode:
    :param disable_notification:
    :param timeout:
    :return:
    """
    method_url = r'sendMessage'
    payload = {'chat_id': str(chat_id), 'text': text}
    if disable_web_page_preview is not None:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup:
        payload['reply_markup'] = _convert_markup(reply_markup)
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['connect-timeout'] = timeout
    return _make_request(token, method_url, params=payload, method='post')


def _convert_markup(markup):
    if isinstance(markup, types.JsonSerializable):
        return markup.to_json()
    return markup
