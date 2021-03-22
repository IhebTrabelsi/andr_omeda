# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Poll
from andr_omeda.andr_update.views.polloption.serializers import PollOptionSerializer
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer

class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True)
    explanation_entities = MessageEntitySerializer()
    class Meta:
        model = Poll
        fields = '__all__'
    
    def create(self, validated_data):
        options_data = validated_data.pop('options', None)
        explanation_entities_data = validated_data.pop('explanation_entities', None)
        
        if options_data:
            options = PollOptionSerializer(**options_data)
            options = options.is_valid()
            options = options.save()
            validated_data['options'] = options
        if explanation_entities_data:
            explanation_entities = MessageEntitySerializer(**data_data)
            explanation_entities = explanation_entities.is_valid()
            explanation_entities = explanation_entities.save()
            validated_data['explanation_entities'] = explanation_entities

        poll = Poll(**validated_data)
        return poll.save()