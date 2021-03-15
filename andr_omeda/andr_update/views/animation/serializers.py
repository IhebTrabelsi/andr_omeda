# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Animation
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class AnimationSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Animation
        fields = '__all__'