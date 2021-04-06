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



class TutorialBotView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        update_id = request.data.pop('update_id', None)
        request.data['update_id'] = {'_id': update_id}
        
        
        _context = unicity_sanitize(data=request.data, context=None)


        serializer = UpdateSerializer(data=request.data, context=_context)
        
        serializer_is_valid = serializer.is_valid(raise_exception=False)
        serializer.save()
        return JsonResponse({"ok": "POST request processed"})