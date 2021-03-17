# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Animation
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class AnimationSerializer(serializers.ModelSerializer):
    thumb = PhotoSizeSerializer()
    class Meta:
        model = Animation
        fields = '__all__'
    
    def create(self, validated_data):
        photo_size_serializer = self.fields['thumb']
        thumb_instance = photo_size_serializer(**validated_data.pop('thumb')).is_valid().save()
        animation_instance = Animation(**validated_data)
        animation_instance.thumb = thumb_instance
        
        return animation_instance.save()
        
