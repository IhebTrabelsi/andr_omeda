# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Document
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer


class DocumentSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer(allow_null=True, required=False)

    class Meta:
        model = Document
        fields = '__all__'
        nested_proxy_field = True

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)

        if thumb_data:
            thumb = PhotoSizeSerializer(data=thumb_data)
            thumb_is_valid = thumb.is_valid(raise_exception=True)
            thumb = thumb.save()
            validated_data['thumb'] = thumb

        document = Document.objects.create(**validated_data)
        return document
