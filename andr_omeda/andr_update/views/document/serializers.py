# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Document
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer

class DocumentSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Document
        fields = '__all__'

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)
        
        if thumb_data:
            thumb = PhotoSizeSerializer(data=thumb_data)
            thumb_is_valid = thumb.is_valid()
            thumb = thumb.save()
            validated_data['thumb'] = thumb
        
        document = Document(**validated_data)
        return document.save()