# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineKeyboardButton, InlineKeyboardButtonList
from andr_omeda.andr_update.views.callbackgame.serializers import CallbackGameSerializer
from andr_omeda.andr_update.views.loginurl.serializers import LoginUrlSerializer

class InlineKeyboardButtonSerializer(serializers.ModelSerializer):
    callback_game = CallbackGameSerializer()
    login_url = LoginUrlSerializer()
    class Meta:
        model = InlineKeyboardButton
        fields = '__all__'

    def create(seelf, validated_data):
        login_url_data = validated_data.pop('login_url', None)
        callback_game_data = validated_data.pop('callback_game', None)
        
        if login_url_data:
            login_url = LoginUrlSerializer(**login_url_data)
            login_url = login_url.is_valid()
            login_url = login_url.save()
            validated_data['login_url'] = login_url
        if callback_game_data:
            callback_game = CallbackGameSerializer(**login_url_data)
            callback_game = callback_game.is_valid()
            callback_game = callback_game.save()
            validated_data['callback_game'] = callback_game

        inline_keyboard_button = InlineKeyboardButton(**validated_data)
        return inline_keyboard_button.save()

class InlineKeyboardButtonListSerializer(serializers.ListSerializer):
    child = InlineKeyboardButtonSerializer()
    def create(self, validated_data):
        inline_keyboard_buttons_lists = [InlineKeyboardButtonList(**button_data) for button_list_data in validated_data]
        for inline_keyboard_buttons_list in inline_keyboard_buttons_lists:
            inline_keyboard_buttons = []
            for inline_keyboard_button in inline_keyboard_buttons_list:
                inline_keyboard_buttons.append(InlineKeyboardButton(**inline_keyboard_button).save())
            inline_keyboard_buttons_list.inline_keyboard_buttons = inline_keyboard_buttons
            inline_keyboard_buttons_list.save()
        return inline_keyboard_buttons_lists