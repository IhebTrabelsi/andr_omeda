# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PollAnswer
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer

class PollAnswerSerializer(serializers.ModelSerializer):
    user = AndruserSerializer()
    class Meta:
        model = PollAnswer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        poll_answer = PollAnswer(**validated_data)
        if user_data:
            user_ser = self.fields['user']
            user = user_ser(**user_data)
            user = user.is_valid().save()
            poll_answer.user = user
        
        return poll_answer.save()
