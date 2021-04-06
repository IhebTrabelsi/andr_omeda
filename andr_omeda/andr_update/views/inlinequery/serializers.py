# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineQuery, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.location.serializers import LocationSerializer

class InlineQuerySerializer(serializers.ModelSerializer):
    inline_query_from = AndruserSerializer()
    location = LocationSerializer()
    
    
    class Meta:
        model = InlineQuery
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('from', None)
        location_data = validated_data.pop('location', None)
        
        if Andruser.user_with_id_exists(user_id=user_data.get('id')):
            user = Andruser.objects.get(pk=user_data.get('id'))
            validated_data['inline_query_from'] = user
        else:
            user = AndruserSerializer(data=user_data)
            user_is_valid = user.is_valid(raise_exception=True)
            user = user.save()
            validated_data['inline_query_from'] = user

        if location_data:
            location = LocationSerializer(data=location_data)
            location_is_valid = location.is_valid(raise_exception=True)
            location = location.save()
            validated_data['location'] = location
        
        inline_query = InlineQuery(**validated_data)
        return inline_query.save()

        
