# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import VoiceChatStarted
class VoiceChatStartedSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceChatStarted
        fields = '__all__'