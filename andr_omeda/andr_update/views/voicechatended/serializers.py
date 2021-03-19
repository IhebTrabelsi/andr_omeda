# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import VoiceChatEnded
class VoiceChatEndedSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceChatEnded
        fields = '__all__'