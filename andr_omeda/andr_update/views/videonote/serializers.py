# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import VideoNote
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer


class VideoNoteSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer(allow_null=True, required=False)

    class Meta:
        model = VideoNote
        fields = '__all__'

    def create(self, validated_data):
        thumb_data = validated_data.pop('thumb', None)

        if thumb_data:
            thumb = PhotoSizeSerializer(data=thumb_data)
            thumb_is_valid = thumb.is_valid(raise_exception=True)
            thumb = thumb.save()
            validated_data['thumb'] = thumb

        video_note = VideoNote(**validated_data)
        return video_note.save()
