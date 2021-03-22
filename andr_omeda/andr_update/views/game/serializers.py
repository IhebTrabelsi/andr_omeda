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
            animation = AnimationSerializer(**animation_data)
            animation = animation.is_valid()
            animation = animation.save()
            validated_data['animation'] = animation
        if text_entities_data:
            text_entities = MessageEntitySerializer(**text_entities_data)
            text_entities = text_entities.is_valid()
            text_entities = text_entities.save()
            validated_data['text_entities'] = text_entities
        if photo_data:
            photo = PhotoSizeSerializer(**photo_data)
            photo = photo.is_valid()
            photo = photo.save()
            validated_data['photo'] = photo

        game = Game(**validated_data)
        return game.save()
        
        