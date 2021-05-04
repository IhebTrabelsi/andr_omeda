from rest_framework import serializers
from .validators import bot_already_exists, \
    bot_with_token_exists

from andr_omeda.andr_bot.models.bot import Bot


class CreateBotSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=50, required=True, allow_blank=False,
                                  validators=[bot_already_exists, ])


class BotERPOwnerSerializer(serializers.Serializer):
    owner_erp_name = serializers.CharField(max_length=255, required=True, allow_blank=False)


class GetBotSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=50, required=True, allow_blank=False,
                                  validators=[bot_already_exists, ])


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
