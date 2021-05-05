# automatically created
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer
from django.views.decorators.csrf import csrf_exempt
from andr_omeda.andr_update.models import Message, Chat
from django.http import JsonResponse
from django.views import View
from andr_omeda.andr_update.utils import unicity_sanitize

from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.tasks import async_serialize_update


class TelegramView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        update_id = request.data.pop('update_id', None)
        request.data['update_id'] = {'_id': update_id}
        print(request.data)
        async_serialize_update.delay(request.data)

        return JsonResponse({"ok": "POST request processed"})
