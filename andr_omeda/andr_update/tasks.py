from celery import shared_task
from django.db import transaction
from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.utils import unicity_sanitize
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer
from andr_omeda.andr_bot.models.bot import BotERPOwner
from andr_omeda.andr_record.models import FlowQueue
from andr_omeda.andr_update import choices
from andr_omeda.andr_update import helpers
import time


@shared_task()
def async_serialize_update(request_data) -> None:
    time.sleep(5)
    with transaction.atomic():
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
        flow_queue = FlowQueue.objects.get(chat=update.message.chat)
        print("==========================FLOWQUEUE========================")
        print(flow_queue.id)
        print("===========================================================", end="\n\n")

        state = flow_queue.queue[-1]

        print("==========================STATE============================")
        print(state)
        print("===========================================================", end="\n\n")

        if state == choices.GREET[0]:
            res = helpers.greet_chat_with_id_in_bot_with_token(update.message.chat.chat_id, token)
            print("==========================RES============================")
            print(res)
            print("===========================================================", end="\n\n")
        else:
            print("==========================RES============================")
            print("MOUCH GREET")
            print("===========================================================", end="\n\n")

        print("===========================================================", end="\n\n")
