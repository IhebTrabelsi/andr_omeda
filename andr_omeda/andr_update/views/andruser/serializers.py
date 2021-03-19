# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Andruser


"""class AndruserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    is_bot = serializers.BooleanField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    language_code = serializers.CharField(required=False)
    can_join_groups = serializers.BooleanField(required=False)
    can_read_all_group_messages = serializers.BooleanField(required=False)
    supports_inline_queries = serializers.BooleanField(required=False)

    def to_internal_value(self, data):

        _id = data.get('id')
        is_bot = data.get('is_bot')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        language_code = data.get('language_code')
        can_join_groups = data.get('can_join_groups')
        can_read_all_group_messages = data.get('can_read_all_group_messages')
        supports_inline_queries = data.get('supports_inline_queries')
        if not _id:
            raise serializers.ValidationError({
                'id': 'This field is required.'
            })

        if not isinstance(update_id, int):
            raise serializers.ValidationError({
                'id': 'This field is not in int form.'
            })

        return {
            'user_id': _id
            'is_bot': is_bot
            'first_name': first_name
            'last_name': last_name
            'username': username
            'language_code': language_code
            'can_join_groups': can_join_groups
            'can_read_all_group_messages': can_read_all_group_messages
            'supports_inline_queries': supports_inline_queries
        }

    def create(self, validated_data):
        return Andruser.objects.create(**validated_data)"""

class AndruserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Andruser
        fields='__all__'
