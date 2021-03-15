# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineKeyboardButton
from andr_omeda.andr_update.views.callbackgame.serializers import CallbackGameSerializer()
from andr_omeda.andr_update.views.loginurl.serializers import LoginUrlSerializer()

class InlineKeyboardButtonSerializer(serializers.ModelSerializer):
    callback_game = CallbackGameSerializer()
    login_url = LoginUrlSerializer()
    class Meta:
        model = InlineKeyboardButton
        fields = '__all__'