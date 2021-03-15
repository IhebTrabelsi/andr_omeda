# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import CallbackGame
class CallbackGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallbackGame
        fields = '__all__'