# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PollAnswer, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer

class PollAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollAnswer
        fields = '__all__'

    def create(self, validated_data):
        __user = None

        validated_data = self.context['validated_data']
        _unicity = self.context.get('unicity')
        _prefix = self.context.get('unicity_prefix')

        user_data = validated_data.pop('from_user')
        
        if _unicity.get(_prefix + '__' + 'from_user', None):
            __user = Andruser.objects.get(pk=_unicity[_prefix + '__' + 'from_user'])
        else:
            if user_data:
                from_user = AndruserSerializer(data=user_data)
                from_user_is_valid = from_user.is_valid(raise_exception=True)
                from_user = from_user.save()
                validated_data['from_user'] = from_user
        
        poll_answer = PollAnswer(**validated_data)

        if __user:
            poll_answer.from_user = __user 
        poll_answer.save()

        return poll_answer.save()
