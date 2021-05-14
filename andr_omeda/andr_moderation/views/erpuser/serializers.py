from rest_framework import serializers
from andr_omeda.andr_bot.models.bot import Bot
from andr_omeda.andr_moderation.serializers_fields.bot import \
    BotPendingModeratedObjectsCountField


class GetErpuserPendingModeratedObjectsBots(serializers.Serializer):
    max_id = serializers.IntegerField(
        required=False,
    )
    count = serializers.IntegerField(
        required=False,
        max_value=20
    )


class PendingModeratedObjectsBotSerializer(serializers.ModelSerializer):
    pending_moderated_objects_count = BotPendingModeratedObjectsCountField()

    class Meta:
        model = Bot
        fields = (
            'id',
            'token',
            'chats',
            'is_webhook_set',
            'erp_owner',
            'created',
            'updated',
            'pending_moderated_objects_count'
        )
