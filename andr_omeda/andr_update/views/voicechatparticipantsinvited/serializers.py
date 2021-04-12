# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import VoiceChatParticipantsInvited
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
class VoiceChatParticipantsInvitedSerializer(serializers.ModelSerializer):
    users = AndruserSerializer(many=True)
    class Meta:
        model = VoiceChatParticipantsInvited
        fields = '__all__'

    def create(self, validated_data):
        users_data = validated_data.pop('users', None)
        if users_data:
            users = AndruserSerializer(data=users_data)
            users_is_valid = users.is_valid(raise_exception=True)
            users = users.save()
            validated_data['users'] = users
        voice_chat_participants_invited = VoiceChatParticipantsInvited(**validated_data)
        return voice_chat_participants_invited.save()