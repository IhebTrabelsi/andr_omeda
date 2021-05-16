from celery import shared_task
from django.db import transaction
from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.utils import unicity_sanitize
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer
from andr_omeda.andr_update.models.update import Update
from andr_omeda.andr_bot.models.erp import BotERPOwner
from andr_omeda.andr_record.models import FlowQueue
from andr_omeda.andr_record.helpers import dispatch_state, \
    get_flow_queue_for_chat_with_id
import time


###########################################################################
#
#
#                               TODO
#
#
###########################################################################

# save last control message/update id sent after responding to user
# and check before sending that the current message.text not eaqual
# to last update.text


###########################################################################

def async_serialize_update(request_data) -> None:
    time.sleep(0)
    print("============================TASK===========================")

    token = request_data.pop('_token_')
    request_data['related_to_bot'] = token
    bot_owner = BotERPOwner.objects.get(bots__token=token)
    bot_owner_name = bot_owner.owner_erp_name
    request_data['for_erp_user'] = bot_owner_name
    print("========================REQUEST_DATA=======================")
    print(request_data)
    print("===========================================================", end="\n\n")

    _context = unicity_sanitize(req_data=request_data)
    print("==========================CONTEXT==========================")
    print(_context)
    print("===========================================================", end="\n\n")

    serializer = UpdateSerializer(data=request_data, context=_context)

    serializer_is_valid = serializer.is_valid(raise_exception=False)
    update = serializer.save()

    message_text = update.message.text
    flow_queue = get_flow_queue_for_chat_with_id(
        chat_id=update.message.chat.chat_id
    )
    print("==========================FLOWQUEUE========================")
    print(flow_queue.id)
    print("===========================================================", end="\n\n")

    state = flow_queue.get_last_queue_state()

    print("==========================STATE============================")
    print(state)
    print("===========================================================", end="\n\n")

    # get last uuid
    no_prev_uuid = flow_queue.no_prev_uuid()
    if not no_prev_uuid:
        print("==========================len(last_update_uuid)>1========================", end="\n\n")
        prev_uuid = flow_queue.get_prev_uuid()
        update_with_last_uuid = Update.objects.get(
            message__chat__chat_id=update.message.chat.chat_id,
            uuid=prev_uuid)

        # BREAKPOINT LOOKING FOR WHERE UUID IS ADDED
        if update_with_last_uuid.message.text == update.message.text:
            print("==========================SENT BY APP========================", end="\n\n")
            return
        else:
            print("==========================dispatch normally========================", end="\n\n")
            dispatch_state(state=state, chat_id=update.message.chat.chat_id, token=token)
    else:
        print("==========================dispatch first event=======================", end="\n\n")
        dispatch_state(state=state, chat_id=update.message.chat.chat_id, token=token)

    print("===========================================================", end="\n\n")
