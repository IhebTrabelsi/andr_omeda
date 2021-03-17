# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Document
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class DocumentSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Document
        fields = '__all__'

    def create(self, validated_data):
        photo_size_serializer = self.fields['thumb']
        thumb_instance = photo_size_serializer(**validated_data.pop('thumb')).is_valid().save()
        document_instance = Document(**validated_data)
        document_instance.thumb = thumb_instance
        
        return document_instance.save()