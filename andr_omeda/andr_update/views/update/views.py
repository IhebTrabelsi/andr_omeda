# automatically created
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from andr_omeda.andr_update.views.update.serializers import UpdateSerializer

class UpdateViewSet(viewsets.ViewSet):
    serializer_class = UpdateSerializer

    @action(detail=True, methods=['post'])
    def rec_update(self, request):
        update_ser = self.serializer_class
        update_ser = update_ser(data=request.data)
        if update_ser.is_valid():
            update_ser.save()
            return Response({'status': 'update saved'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST) 