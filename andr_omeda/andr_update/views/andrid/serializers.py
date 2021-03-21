from rest_framework import serializers
from andr_omeda.andr_update.models.andrid import Andrid


class AndridSerializer(serializers.BaseSerializer):
    week_order = serializers.IntegerField(read_only=True)
    _id = serializers.CharField(required=True, label="_id")
    created = serializers.DateTimeField(read_only=True)
    
    def to_internal_value(self, data):
        if not data:
            raise serializers.ValidationError({
                'update_id': 'This field is required.'
            })
        
        if not isinstance(data, int):
            raise serializers.ValidationError({
                'update_id': 'This field is not in int form.'
            })
        
        return {
            '_id': data
        }
    
    def create(self, validated_data):
        if not isinstance(validated_data, int):
            raise serializers.ValidationError({
                'update_id': 'This field is not in int form.'
            })
        return Andrid.create_andrid(_id=validated_data)

    
