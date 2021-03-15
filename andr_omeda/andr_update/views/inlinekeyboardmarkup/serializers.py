# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineKeyboardMarkup
from andr_omeda.andr_update.views.inlinekeyboardbutton.serializers import InlineKeyboardButtonSerializer()

class InlineKeyboardMarkupSerializer(serializers.ModelSerializer):
    inline_keyboard = InlineKeyboardButton(many=True)
    class Meta:
        model = InlineKeyboardMarkup
        fields = '__all__'