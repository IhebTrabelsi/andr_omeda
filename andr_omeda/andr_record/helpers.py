from andr_omeda.andr_update import choices
from andr_omeda.andr_update import helpers


def dispatch_state(state, chat_id, token):
    if state == choices.GREET[0]:
        res = helpers.greet_chat_with_id_in_bot_with_token(chat_id, token)
        print("==========================RES============================")
        print(res)
        print("===========================================================", end="\n\n")
    else:
        print("==========================RES============================")
        print("MOUCH GREET")
        print("===========================================================", end="\n\n")
