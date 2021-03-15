# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import LoginUrl
class LoginUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUrl
        fields = '__all__'