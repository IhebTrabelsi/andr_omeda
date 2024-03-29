# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Poll
from andr_omeda.andr_update.views.polloption.serializers import PollOptionSerializer
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer

class PollSerializer(serializers.ModelSerializer):
    options = serializers.ListField(
        child=PollOptionSerializer(),
        required=False,
        allow_empty=True 
    )
    explanation_entities = serializers.ListField(
        child=MessageEntitySerializer(),
        required=False, 
        allow_empty=True
    )

    class Meta:
        model = Poll
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data = self.context['validated_data']
        _lists = self.context['lists']

        options_data = validated_data.pop('options', None)
        explanation_entities_data = validated_data.pop('explanation_entities', None)

        validated_data['poll_id'] = validated_data['id']
        del validated_data['id']

        poll = Poll.objects.create(**validated_data)
        
        if _lists.get('poll__options', None):
            for poll__option in _lists['poll__options']:
                option = PollOptionSerializer(data=poll__option)
                option_is_valid = option.is_valid()
                option_instance = option.save()
                option_instance.poll = poll
                option_instance.save()
        if _lists.get('poll__explanation_entities', None):
            for poll__explanation_entity in _lists['poll__explanation_entities']:
                explanation_entity = MessageEntitySerializer(data=poll__explanation_entity)
                explanation_entity_is_valid = explanation_entity.is_valid()
                explanation_entity_instance = explanation_entity.save()
                explanation_entity_instance.poll = poll 
                explanation_entity_instance.save()
        
        return poll