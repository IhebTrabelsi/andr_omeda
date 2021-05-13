import telebot
from andr_omeda.andr_base.utils.telegram_requester import send_message
from andr_omeda.andr_base.utils.common_types import yes_no_keyboard_markup


def greet_chat_with_id_in_bot_with_token(chat_id, token):
    greet_text = r'Yeaaaaah boy , accept terms ?'

    res = send_message(
        token, chat_id, greet_text,
        disable_web_page_preview=None, reply_to_message_id=None,
        reply_markup=yes_no_keyboard_markup, parse_mode=None,
        disable_notification=None, timeout=None
    )
    return res