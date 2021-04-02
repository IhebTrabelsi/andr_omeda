# automatically created
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer
from django.views.decorators.csrf import csrf_exempt

class UpdateViewSet(viewsets.ViewSet):
    serializer_class = UpdateSerializer

    def create(self, request, **kwargs):
        update_ser = self.serializer_class
        update_ser = update_ser(data=request.data)
        if update_ser.is_valid():
            update_ser.save()
            return Response({'status': 'update saved'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST) 

from django.http import JsonResponse
from django.views import View
class TutorialBotView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        update_id = request.data.pop('update_id', None)
        request.data['update_id'] = {'_id': update_id}
        serializer = UpdateSerializer(data=request.data, context={'request': request})
        print(request.data)
        serializer_is_valid = serializer.is_valid(raise_exception=False)
        print(777)
        print(serializer.errors)
        print(serializer_is_valid)
        print("\n\n\n")
        serializer.save()
        return JsonResponse({"ok": "POST request processed"})