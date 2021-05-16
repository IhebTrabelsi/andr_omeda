from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction

from andr_omeda.andr_moderation.views.moderated_object.serializers import \
    UpdateModeratedObjectSerializer, ModeratedObjectSerializer, \
    ModeratedObjectLogSerializer, ApproveModeratedObjectSerializer

from andr_omeda.andr_bot.models.erp import BotERPOwner


class ModeratedObjectItem(APIView):
    permission_classes = (AllowAny,)

    def patch(self, request, erp_name, moderated_object_id):
        request_data = request.data.copy()

        request_data['moderated_object_id'] = moderated_object_id
        serializer = UpdateModeratedObjectSerializer(data=request_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        description = data.get('description')
        category_id = data.get('category_id')
        moderated_object_id = data.get('moderated_object_id')

        erpuser = BotERPOwner.objects.get(owner_erp_name=erp_name)

        with transaction.atomic():
            moderated_object = erpuser.update_moderated_object_with_id(moderated_object_id=moderated_object_id,
                                                                       description=description, category_id=category_id, )

        moderated_object_serializer = ModeratedObjectSerializer(moderated_object,
                                                                context={"request": request, "erp_name": erp_name})

        return Response(moderated_object_serializer.data, status=status.HTTP_200_OK)


class ApproveModeratedObject(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, erp_name, moderated_object_id):
        serializer = ApproveModeratedObjectSerializer(data={
            'moderated_object_id': moderated_object_id
        }, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        moderated_object_id = data.get('moderated_object_id')

        erpuser = BotERPOwner.objects.get(owner_erp_name=erp_name)

        with transaction.atomic():
            moderated_object = erpuser.approve_moderated_object_with_id(moderated_object_id=moderated_object_id, )

        moderated_object_serializer = ModeratedObjectSerializer(moderated_object,
                                                                context={"request": request, "erp_name": erp_name})

        return Response(moderated_object_serializer.data, status=status.HTTP_200_OK)


class RejectModeratedObject(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, erp_name, moderated_object_id):
        serializer = ApproveModeratedObjectSerializer(data={
            'moderated_object_id': moderated_object_id
        }, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        moderated_object_id = data.get('moderated_object_id')

        erpuser = BotERPOwner.objects.get(owner_erp_name=erp_name)

        with transaction.atomic():
            moderated_object = erpuser.reject_moderated_object_with_id(moderated_object_id=moderated_object_id, )

        moderated_object_serializer = ModeratedObjectSerializer(moderated_object,
                                                                context={"request": request, "erp_name": erp_name})

        return Response(moderated_object_serializer.data, status=status.HTTP_200_OK)


class ModeratedObjectLogs(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, erp_name, moderated_object_id):
        request_data = request.query_params.dict()

        request_data['moderated_object_id'] = moderated_object_id
        serializer = GetModeratedObjectLogsSerializer(data=request_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        count = data.get('count')
        max_id = data.get('max_id')
        moderated_object_id = data.get('moderated_object_id')

        erpuser = BotERPOwner.objects.get(owner_erp_name=erp_name)

        with transaction.atomic():
            moderated_object_logs = erpuser.get_logs_for_moderated_object_with_id(max_id=max_id,
                                                                                  moderated_object_id=moderated_object_id).order_by(
                '-id')[:count]

        moderated_object_logs_serializer = ModeratedObjectLogSerializer(moderated_object_logs, many=True,
                                                                        context={"request": request, "erp_name": erp_name})

        return Response(moderated_object_logs_serializer.data, status=status.HTTP_200_OK)
