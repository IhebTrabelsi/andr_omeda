# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Game
from andr_omeda.andr_update.views.animation.serializers import AnimationSerializer
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer

class GameSerializer(serializers.ModelSerializer):
    animation = AnimationSerializer()
    text_entities = MessageEntitySerializer(many=True)
    photo = PhotoSizeSerializer(many=True)
    class Meta:
        model = Game
        fields = '__all__'

    def create(self, validated_data):
        animation_data = validated_data.pop('animation', None)
        text_entities_data = validated_data.pop('text_entities', None)
        photo_data = validated_data.pop('photo', None)
        

        if animation_data:
            animation = AnimationSerializer(data=animation_data)
            animation_is_valid = animation.is_valid(raise_exception=True)
            animation = animation.save()
            validated_data['animation'] = animation
        if text_entities_data:
            text_entities = MessageEntitySerializer(data=text_entities_data)
            text_entities_is_valid = text_entities.is_valid(raise_exception=True)
            text_entities = text_entities.save()
            validated_data['text_entities'] = text_entities
        if photo_data:
            photo = PhotoSizeSerializer(data=photo_data)
            photo_is_valid = photo.is_valid(raise_exception=True)
            photo = photo.save()
            validated_data['photo'] = photo

        game = Game(**validated_data)
        return game.save()
        
        