from andr_omeda.andr_base.utils import types

accept_terms_yes_button = types.KeyboardButton(
    text=r'yes',
    request_contact=True,
    request_location=True
)

accept_terms_no_button = types.KeyboardButton(
    text=r'no'
)

yes_no_keyboard_markup = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=None,
    row_width=2
).row(
    accept_terms_yes_button,
    accept_terms_no_button
)
