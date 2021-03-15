# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Video
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class VideoSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Video
        fields = '__all__'