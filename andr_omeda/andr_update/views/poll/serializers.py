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
        poll = Poll(**validated_data)
        if options_data:
            options_ser = self.fields['options']
            options = options_ser(**options_data)
            options = options.is_valid().save()
            poll.options = options
        if explanation_entities_data:
            explanation_entities_ser = self.fields['explanation_entities']
            explanation_entities = explanation_entities_ser(**data_data)
            explanation_entities = explanation_entities.is_valid().save()
            poll.explanation_entities = explanation_entities

        return poll.save()