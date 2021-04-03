# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatInviteLink, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
class ChatInviteLinkSerializer(serializers.ModelSerializer):
    creator = AndruserSerializer()
    class Meta:
        model = ChatInviteLink
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('creator', None)
        chat_invite_link = ChatInviteLink(**validated_data)
        if user:
            chat_invite_link.creator = user
        return chat_invite_link.save()