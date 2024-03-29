# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Animation
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer


class AnimationSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer(allow_null=True, required=False)

    class Meta:
        model = Animation
        fields = '__all__'

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)

        if thumb_data:
            thumb = PhotoSizeSerializer(data=thumb_data)
            thumb_is_valid = thumb.is_valid(raise_exception=True)
            thumb = thumb.save()
            validated_data['thumb'] = thumb

        animation = Animation(**validated_data)
        return animation.save()
