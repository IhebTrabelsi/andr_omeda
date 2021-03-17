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
        photo_size_serializer = self.fields['thumb']
        thumb_instance = photo_size_serializer(**validated_data.pop('thumb')).is_valid().save()
        audio_instance = Audio(**validated_data)
        audio_instance.thumb = thumb_instance
        
        return audio_instance.save()