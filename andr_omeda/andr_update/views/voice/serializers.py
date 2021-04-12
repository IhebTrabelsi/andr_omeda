# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Voice
class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = '__all__'
    
