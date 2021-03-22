# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineKeyboardMarkup
from andr_omeda.andr_update.views.inlinekeyboardbutton.serializers import InlineKeyboardButtonListSerializer

class InlineKeyboardMarkupSerializer(serializers.ModelSerializer):
    inline_keyboard_button_lists = InlineKeyboardButtonListSerializer(many=True)
    class Meta:
        model = InlineKeyboardMarkup
        fields = '__all__'
    
    def create(self, validated_data):
        inline_keyboard_button_lists_data = validated_data.pop('inline_keyboard', None)
        inline_keyboard_button_lists = []
        for kb_list in inline_keyboard_button_lists_data:
            inline_keyboard_button_lists.append(InlineKeyboardButtonListSerializer(**kb_list))
        validated_data['inline_keyboard_button_lists'] = inline_keyboard_button_lists
        inline_keyboard_markup = InlineKeyboardMarkup(**validated_data)
        return inline_keyboard_markup.save()
        

            