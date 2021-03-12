from rest_framework import serializers
from andr_omeda.andr_update.models.andrid import Andrid


class AndridSerializer(serializers.BaseSerializer):
    week_order = serializers.IntegerField(read_only=True)
    _id = serializers.CharField(required=True, label="_id")
    created = serializers.DateTimeField(read_only=True)
    
    def to_internal_value(self, data):
        update_id = data.get('update_id')
        if not update_id:
            raise serializers.ValidationError({
                'update_id': 'This field is required.'
            })
        
        if not isinstance(update_id, int):
            raise serializers.ValidationError({
                'update_id': 'This field is not in int form.'
            })
        
        return {
            '_id': update_id
        }
    
    def create(self, validated_data):
        return Andrid.create_andrid(**validated_data)

    
