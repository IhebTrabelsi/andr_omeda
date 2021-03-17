# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatInviteLink, Andruser
class ChatInviteLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatInviteLink
        fields = '__all__'

    def create(self, validated_data):
        user = Andruser.get_user_with_id(user_id= validated_data.pop('user').get('user_id'))
        chat_invite_link = ChatInviteLink(**validated_data)
        chat_invite_link.creator = user 

        chat_invite_link.save()

        return chat_invite_link