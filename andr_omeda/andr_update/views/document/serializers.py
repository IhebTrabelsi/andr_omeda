# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Document
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class DocumentSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Document
        fields = '__all__'