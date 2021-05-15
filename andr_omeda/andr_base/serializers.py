from andr_omeda.andr_update.models.chat import Chat
from rest_framework import serializers


class CommonPublicChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = (
            'chat_id',
            'type',
            'username',
        )
