from rest_framework.views import APIView
from .serializers import BotERPOwnerSerializer, CreateBotSerializer, GetBotSerializer, \
    BotSerializer
from andr_omeda.andr_bot.models.bot import BotERPOwner, Bot
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class Bots(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, user_erp_name, token):
        erp_owner_data = request.data.get('erp_owner_name', None)
        owner_serializer = BotERPOwnerSerializer(
            data={"owner_erp_name": erp_owner_data}
        )
        print(owner_serializer, end='\n\n')
        owner_serializer.is_valid(raise_exception=True)
        print(owner_serializer.errors, end='\n\n')
        owner_name = owner_serializer.validated_data
        owner = BotERPOwner.objects.get_or_create(
            owner_erp_name=owner_name
        )[0]

        bot_serializer = CreateBotSerializer(data=request.data)
        bot_serializer.is_valid(raise_exception=True)
        bot_token = bot_serializer.validated_data
        bot = Bot.objects.create(
            token=bot_token,
            erp_owner=owner
        )
        return Response({
            'status': 'ok'
        }, status=status.HTTP_200_OK)

    def get(self, request, user_erp_name, token):
        request_data = self._get_request_data(request, user_erp_name, token)
        owner_name = request_data.pop('user_erp_name', '')
        try:
            BotERPOwner.owner_with_name_exists(
                user_erp_name=owner_name
            )
        except ValidationError as e:
            return Response({
                'error': e
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = GetBotSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        token_data = serializer.validated_data

        bot = BotERPOwner.get_bot_with_token_for_user_with_name(token_data, owner_name)

        bot_serializer = BotSerializer(bot)

        return Response({
            bot_serializer.data
        }, status=status.HTTP_200_OK)

    def _get_request_data(self, request, user_erp_name, token):
        request_data = request.data.copy()
        request_data['token'] = token
        request_data['user_erp_name'] = user_erp_name
        return request_data
