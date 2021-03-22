# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Sticker
from andr_omeda.andr_update.views.maskposition.serializers import MaskPositionSerializer
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer

class StickerSerializer(serializers.ModelSerializer):
    mask_position = MaskPositionSerializer()
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Sticker
        fields = '__all__'

    def create(self, validated_data):
        mask_position_data = validated_data.pop('mask_position', None)
        thumb_data = validated_data.pop('thumb', None)
        
        if mask_position_data:
            mask_position = MaskPositionSerializer(**mask_position_data)
            mask_position = mask_position.is_valid()
            mask_position = mask_position.save()
            validated_data['mask_position'] = mask_position
        if thumb_data:
            thumb = PhotoSizeSerializer(**thumb_data)
            thumb = thumb.is_valid()
            thumb = thumb.save()
            validated_data['thumb'] = thumb

        sticker = Stricker(**validated_data)
        return sticker.save()