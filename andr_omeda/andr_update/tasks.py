from celery import shared_task
from django.db import transaction
from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.utils import unicity_sanitize
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer
from andr_omeda.andr_bot.models.bot import BotERPOwner


@shared_task
def async_serialize_update(request_data) -> None:
    with transaction.atomic():

        token = request_data.pop('_token_')
        request_data['related_to_bot'] = token
        bot_owner = BotERPOwner.objects.get(bots__token=token)
        bot_owner_name = bot_owner.owner_erp_name
        request_data['for_erp_user'] = bot_owner_name

        print(request_data)

        _context = unicity_sanitize(req_data=request_data)
        print(_context)

        serializer = UpdateSerializer(data=request_data, context=_context)

        serializer_is_valid = serializer.is_valid(raise_exception=False)
        print("\n\n")

        serializer.save()
