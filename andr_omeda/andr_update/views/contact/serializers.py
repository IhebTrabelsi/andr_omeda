# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'