from celery import shared_task
from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.utils import unicity_sanitize
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer


@shared_task
def async_serialize_update(request_data) -> None:
    try:
        print(request_data)

        _context = unicity_sanitize(req_data=request_data)
        print(_context)

        serializer = UpdateSerializer(data=request_data, context=_context)

        serializer_is_valid = serializer.is_valid(raise_exception=False)
        print("\n\n")

        serializer.save()
    except Exception as e:
        raise Exception("Celery related exception in update task!")
