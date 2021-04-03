# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PollAnswer, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer

class PollAnswerSerializer(serializers.ModelSerializer):
    user = AndruserSerializer()
    class Meta:
        model = PollAnswer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        if Andruser.user_with_id_exists(user_id=user_data.get('id')):
            user = Andruser.objects.get(pk=user_data.get('id'))
            validated_data['user'] = user
        else:
            user = AndruserSerializer(data=user_data)
            user_is_valid = user.is_valid()
            user = user.save()
            validated_data['user'] = user
        
        poll_answer = PollAnswer(**validated_data)
        return poll_answer.save()
