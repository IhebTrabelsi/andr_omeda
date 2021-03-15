# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Game
from andr_omeda.andr_update.views.animation.serializers import AnimationSerializer()
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer()
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()

class GameSerializer(serializers.ModelSerializer):
    animation = AnimationSerializer()
    text_entities = MessageEntitySerializer(many=True)
    explanation_entities = MessageEntitySerializer(many=True)
    photo = PhotoSizeSerializer(many=True)
    class Meta:
        model = Game
        fields = '__all__'