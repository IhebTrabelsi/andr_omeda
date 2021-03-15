# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Audio
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class AudioSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Audio
        fields = '__all__'