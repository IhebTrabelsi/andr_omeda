from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from andr_omeda.andr_moderation.views.erpuser.serializers import \
    GetErpuserPendingModeratedObjectsBots

from andr_omeda.andr_bot.models.erp import BotERPOwner


class ChatPendingModeratedObjectsBots(APIView):
    permission_classes = (AllowAny,)

    def get(self, erp_name, request):
        query_params = request.query_params.dict()

        serializer = GetErpuserPendingModeratedObjectsBots(data=query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        count = data.get('count', 10)
        max_id = data.get('max_id')

        erpuser = BotERPOwner.objects.get(owner_erp_name=erp_name)

        bots = erpuser.get_pending_moderated_objects_bots(max_id=max_id, ).order_by('-id')[
            :count]

        response_serializer = PendingModeratedObjectsBotSerializer(bots, many=True,
                                                                   context={"request": request, "erp_name": errp_name})

        return Response(response_serializer.data, status=status.HTTP_200_OK)
