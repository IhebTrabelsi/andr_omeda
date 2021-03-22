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
            user = AndruserSerializer(**from_user_data)
            user = user.is_valid()
            user = user.save()
            validated_data['from'] = user

        if location_data:
            location = LocationSerializer(**location_data)
            location = location.is_valid()
            location = location.save()
            validated_data['location'] = location
        chosen_inline_result = ChosenInlineResult(**validated_data)
        return chosen_inline_result.save()
        