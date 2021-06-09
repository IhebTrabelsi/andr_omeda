from andr_omeda.andr_update import choices
from andr_omeda.andr_update import helpers
from andr_omeda.andr_moderation.models import ModeratedObject
from andr_omeda.andr_record.models import FlowQueue
from andr_omeda.andr_update.models.chat import Chat


def get_flow_queue_for_chat_with_id(chat_id):
    chat = Chat.objects.get(chat_id=chat_id)
    if chat:
        return FlowQueue.objects.get(chat=chat)
    else:
        raise Exception('chat does not exist')


def dispatch_state(update, queue, chat_id, token):
    state = queue.get_last_queue_state()
    print("~~"*20, end='\n')
    print(state)
    moderation_approved = ModeratedObject.check_moderation_approved(chat_id=chat_id, token=token)
    if not moderation_approved:
        state = choices.WAITING_FOR_APPROVAL[0]

    if state == choices.WAITING_FOR_APPROVAL[0]:

        if moderation_approved:
            queue = get_flow_queue_for_chat_with_id(chat_id=chat_id)
            queue.append_state(choices.GREET[0])

        else:
            res = helpers.info_chat_must_be_approved(queue, chat_id, token)
            print("==========================RES============================")
            print(res)
            print("===========================================================", end="\n\n")

    else:
        if state == choices.GREET[0]:
            res = helpers.greet_chat_with_id_in_bot_with_token(queue, chat_id, token)
            print("==========================RES============================")
            print(res)
            print("===========================================================", end="\n\n")
        else:
            if state == choices.WAITING_FOR_TERMS_ACCEPT[0]:
                if update.message.text == 'yes':
                    res = helpers.info_terms_accepted(queue, chat_id, token)
            else:
                if state == choices.IDLE[0]:
                    if update.message.text == '1':
                        res = helpers.info_placeholder(queue, chat_id, token)
                    else:
                        res = helpers.info_idle(queue, chat_id, token)
