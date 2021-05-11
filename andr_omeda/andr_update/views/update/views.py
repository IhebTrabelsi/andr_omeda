# automatically created
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from andr_omeda.andr_update.models import Message, Chat
from django.http import JsonResponse
from django.views import View
from andr_omeda.andr_update.utils import unicity_sanitize
from celery import chain

from andr_omeda.utils.colorify import colorify
from andr_omeda.andr_update.tasks import async_serialize_update


class TelegramView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, token, *args, **kwargs):
        update_id = request.data.pop('update_id', None)
        request.data['update_id'] = {'_id': update_id}
        request.data['_token_'] = token
        print("============================VIEW===========================")
        print(request.data)
        print("===========================================================", end="\n\n")
        transaction.on_commit(async_serialize_update.s(request.data).delay)

        return JsonResponse({"ok": "POST request processed"})
