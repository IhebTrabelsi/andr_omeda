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
        user_data = validated_data.pop('creator', None)
        if Andruser.user_with_id_exists(user_id=user_data.get('id')):
            user = Andruser.objects.get(pk=user_data.get('id'))
            validated_data['creator'] = user
        else:
            user = AndruserSerializer(data=user_data)
            user_is_valid = user.is_valid()
            user = user.save()
            validated_data['creator'] = user
        
        chat_invite_link = ChatInviteLink(**validated_data)
        return chat_invite_link.save()