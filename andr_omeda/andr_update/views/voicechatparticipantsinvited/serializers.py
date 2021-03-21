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
        users_ser = self.fields['users']
        users = users_ser(**validated_data)
        return users.is_valid().save()