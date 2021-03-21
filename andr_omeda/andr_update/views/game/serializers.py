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
        game = Game(**validated_data)

        if animation_data:
            animation_ser = self.fields['animation']
            animation = animation_ser(**animation_data)
            animation = animation.is_valid().save()
            game.animation = animation
        if text_entities_data:
            text_entities_ser = self.fields['text_entities']
            text_entities = text_entities_ser(**text_entities_data)
            text_entities = text_entities.is_valid().save()
            game.text_entities = text_entities
        if photo_data:
            photo_ser = self.fields['photo']
            photo = photo_ser(**photo_data)
            photo = photo.is_valid().save()
            game.photo_data = photo_data

        return game.save()
        
        