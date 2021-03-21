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
        video = Video(**validated_data)
        if thumb_data:
            thumb_ser = self.fields['thumb']
            thumb = thumb_ser(**thumb_data)
            thumb = thumb.is_valid().save()
            video.thumb = thumb
        
        return video.save()