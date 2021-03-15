# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatPhoto
class ChatPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatPhoto
        fields = '__all__'