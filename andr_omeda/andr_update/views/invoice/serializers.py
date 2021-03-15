# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Invoice
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'