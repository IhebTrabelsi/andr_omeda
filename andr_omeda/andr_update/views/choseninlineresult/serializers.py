# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChosenInlineResult, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.location.serializers import LocationSerializer

class ChosenInlineResultSerializer(serializers.ModelSerializer):
    from_user = AndruserSerializer()
    location = LocationSerializer()
    class Meta:
        model = ChosenInlineResult
        fields = '__all__'

    def create(self, validated_data):
        from_user_data = validated_data.pop('from', None)
        location_data = validated_data.pop('location', None)

        if Andruser.user_with_id_exists(user_id=from_user_data.get('id')):
            user = Andruser.objects.get(pk=from_user_data.get('id'))
            validated_data['from'] = user
        else:
            user = AndruserSerializer(data=from_user_data)
            user_is_valid = user.is_valid(raise_exception=True)
            user = user.save()
            validated_data['from'] = user

        if location_data:
            location = LocationSerializer(data=location_data)
            location_is_valid = location.is_valid(raise_exception=True)
            location = location.save()
            validated_data['location'] = location
        chosen_inline_result = ChosenInlineResult(**validated_data)
        return chosen_inline_result.save()
        