import telebot
from andr_omeda.andr_base.utils.telegram_requester import send_message
from andr_omeda.andr_base.utils.common_types import yes_no_keyboard_markup, \
    idle_keyboard_markup
from andr_omeda.andr_update import choices


def greet_chat_with_id_in_bot_with_token(queue, chat_id, token):
    queue.append_state(choices.WAITING_FOR_TERMS_ACCEPT[0])
    greet_text = r'Yeaaaaah boy chat approved, accept terms ?'

    res = send_message(
        token, chat_id, greet_text,
        disable_web_page_preview=None, reply_to_message_id=None,
        reply_markup=yes_no_keyboard_markup, parse_mode=None,
        disable_notification=None, timeout=None
    )
    return res


def info_chat_must_be_approved(queue, chat_id, token):
    info_text = r'conversation must be approved from owner'

    res = send_message(
        token, chat_id, info_text,
        disable_web_page_preview=None, reply_to_message_id=None,
        reply_markup=yes_no_keyboard_markup, parse_mode=None,
        disable_notification=None, timeout=None
    )
    return res


def info_terms_accepted(queue, chat_id, token):
    queue.append_state(choices.IDLE[0])
    info_text = r'you have accepted terms !'

    res = send_message(
        token, chat_id, info_text,
        disable_web_page_preview=None, reply_to_message_id=None,
        reply_markup=yes_no_keyboard_markup, parse_mode=None,
        disable_notification=None, timeout=None
    )
    return res


def info_idle(queue, chat_id, token):
    info_text = r'Please chose an action: \n1: get last steuererklaerung.'

    res = send_message(
        token, chat_id, info_text,
        disable_web_page_preview=None, reply_to_message_id=None,
        reply_markup=idle_keyboard_markup, parse_mode=None,
        disable_notification=None, timeout=None
    )
    return res


def info_placeholder(queue, chat_id, token):
    info_text = r'placeholder'

    res = send_message(
        token, chat_id, info_text,
        disable_web_page_preview=None, reply_to_message_id=None,
        reply_markup=idle_keyboard_markup, parse_mode=None,
        disable_notification=None, timeout=None
    )
    return res
