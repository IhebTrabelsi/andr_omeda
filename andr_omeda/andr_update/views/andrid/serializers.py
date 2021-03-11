from rest_framework import serializers
from andr_omeda.andr_update.models.andrid import Andrid


class AndridSerializer(serializers.BaseSerializer):
    _id = serializers.CharField(required=True, label="andrid_id")
    
    def to_internal_value(self, data):
        update_id = data.get('update_id')
        if not update_id:
            raise serializers.ValidationError({
                'update_id': 'This field is required.'
            })
        
        if not isinstance(update_id, str):
            raise serializers.ValidationError({
                'update_id': 'This field is not in str form.'
            }) 
    
    def create(self, validated_data):
        return Andrid.create_andrid(**validated_data)

    
