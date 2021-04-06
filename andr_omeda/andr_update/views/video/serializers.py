# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Video
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer

class VideoSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)
        
        if thumb_data:
            thumb = PhotoSizeSerializer(data=thumb_data)
            thumb_is_valid = thumb.is_valid(raise_exception=True)
            thumb = thumb.save()
            validated_data['thumb'] = thumb
        
        video = Video(**validated_data)
        return video.save()