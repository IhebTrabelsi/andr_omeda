# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import VideoNote
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class VideoNoteSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = VideoNote
        fields = '__all__'