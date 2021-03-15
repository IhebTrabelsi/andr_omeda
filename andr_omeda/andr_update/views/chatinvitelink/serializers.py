# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatInviteLink
class ChatInviteLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatInviteLink
        fields = '__all__'