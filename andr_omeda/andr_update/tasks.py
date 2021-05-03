from celery import shared_task
from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.utils import unicity_sanitize
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer


@shared_task
def async_serialize_update(request_data) -> None:
    try:
        colorify('\n\n' + '='*100 + '\n\n', fore='RED', back='RED')
        #colorify(request_data, fore='GREEN', back='WHITE', highlight="START !")

        _context = unicity_sanitize(req_data=request_data)
        #colorify(_context, fore='BLACK', back='YELLOW', highlight="UPDATE CONTEXT !")

        serializer = UpdateSerializer(data=request_data, context=_context)

        serializer_is_valid = serializer.is_valid(raise_exception=False)
        print("\n\n")
        colorify(serializer_is_valid, fore='BLUE', back='WHITE')
        colorify('\n' + str(serializer.errors) + '\n', fore='BLUE', back='WHITE')

        serializer.save()
        colorify('\n\n' + '='*100 + '\n\n', fore='RED', back='RED')
    except Exception as e:
        raise Exception("Celery related exception in update task!")
