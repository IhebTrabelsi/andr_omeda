# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Audio
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer

class AudioSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Audio
        fields = '__all__'

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)
        
        if thumb_data:
            thumb_ser = self.fields['thumb']
            thumb = PhotoSizeSerializer()(**thumb_data)
            thumb_is_valid = thumb.is_valid()
            thumb = thumb.save()
            audio.thumb = thumb
        
        audio = Audio(**validated_data)
        return audio.save()