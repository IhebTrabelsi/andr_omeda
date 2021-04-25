# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Andruser


class AndruserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andruser
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'validators': []},
        }

    def create(self, validated_data):
        if Andruser.user_with_id_exists(validated_data.get('user_id')):
            user = Andruser.objects.get(pk=validated_data.get('user_id'))
        else:

            user = Andruser.objects.create(**validated_data)

        return user


class AndruserListSerializer(serializers.Serializer):
    def create(self, validated_data):
        _lists = None
        if self.context:
            validated_data = self.context['validated_data']
            if self.context.get('lists', None):
                _lists = self.context['lists']
        if _lists:
            _users = []
            new_chat_members_data = _lists['message__new_chat_members']
            for member in new_chat_members_data:
                if Andruser.user_with_id_exists(user_id=member['id']):
                    _users.append(Andruser.objects.get(user_id=member['id']))
                else:
                    new_user = Andruser.objects.create(**member)
                    _users.append(new_user)
            return _users
        return []
