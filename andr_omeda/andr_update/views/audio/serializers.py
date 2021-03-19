# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Audio
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class AudioSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Audio
        fields = '__all__'

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)
        audio = Audio(**validated_data)
        if thumb_data:
            thumb_ser = self.fields['thumb']
            thumb = thumb_ser(**thumb_data)
            thumb = thumb.is_valid().save()
            audio.thumb = thumb
        
        return audio.save()