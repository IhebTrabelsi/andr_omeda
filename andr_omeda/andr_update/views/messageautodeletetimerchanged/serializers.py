from rest_framework import serializers
from andr_omeda.andr_update.models import MessageAutoDeleteTimerChanged


class MessageAutoDeleteTimerChangedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageAutoDeleteTimerChanged
        fields = '__all__'
