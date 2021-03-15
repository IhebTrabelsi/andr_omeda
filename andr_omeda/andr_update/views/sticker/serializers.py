# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Sticker
from andr_omeda.andr_update.views.maskposition.serializers import MaskPositionSerializer()
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class StickerSerializer(serializers.ModelSerializer):
    mask_position = MaskPositionSerializer()
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Sticker
        fields = '__all__'