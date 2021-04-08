# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChosenInlineResult, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.location.serializers import LocationSerializer

class ChosenInlineResultSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = ChosenInlineResult
        fields = '__all__'

    def create(self, validated_data):
        __user = None

        validated_data = self.context['validated_data']
        _unicity = self.context.get('unicity')
        _prefix = self.context.get('unicity_prefix')

        user_data = validated_data.pop('from', None)
        location_data = validated_data.pop('location', None)

        if _unicity.get(_prefix + '__' + 'from_user', None):
            __user = Andruser.objects.get(pk=_unicity[_prefix + '__' + 'from_user'])
        else:
            if user_data:
                from_user = AndruserSerializer(data=user_data)
                from_user_is_valid = from_user.is_valid(raise_exception=True)
                from_user = from_user.save()
                validated_data['from_user'] = from_user

        if location_data:
            location = LocationSerializer(data=location_data)
            location_is_valid = location.is_valid(raise_exception=True)
            location = location.save()
            validated_data['location'] = location
        chosen_inline_result = ChosenInlineResult(**validated_data)

        if __user:
            chosen_inline_result.from_user = __user 
        
        chosen_inline_result.save()
        return chosen_inline_result.save()
        