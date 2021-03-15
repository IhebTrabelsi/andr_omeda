# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PhotoSize
class PhotoSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSize
        fields = '__all__'