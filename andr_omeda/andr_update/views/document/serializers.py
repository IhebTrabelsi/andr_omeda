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
        document = Document(**validated_data)
        if thumb_data:
            thumb_ser = self.fields['thumb']
            thumb = thumb_ser(**thumb_data)
            thumb = thumb.is_valid().save()
            document.thumb = thumb
        
        return document.save()