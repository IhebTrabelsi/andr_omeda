# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.views.andrid.serializers import AndridSerializer
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.message.serializers import MessageSerializer()
from andr_omeda.andr_update.views.inlinequery.serializers import InlineQuerySerializer()
from andr_omeda.andr_update.views.choseninlineresult.serializers import ChosenInlineResultSerializer()
from andr_omeda.andr_update.views.callbackquery.serializers import CallbackQuerySerializer()
from andr_omeda.andr_update.views.shippingquery.serializers import ShippingQuerySerializer()
from andr_omeda.andr_update.views.precheckoutquery.serializers import PreCheckoutQuerySerializer()
from andr_omeda.andr_update.views.poll.serializers import PollSerializer()
from andr_omeda.andr_update.views.pollanswer.serializers import PollAnswerSerializer()
from andr_omeda.andr_update.views.chatmemberupdated.serializers import ChatMemberUpdatedSerializer()


class UpdateSerializer(serializers.Serializer):
    update_id = AndridSerializer(required=True)
    message = MessageSerializer(required=False)
    edited_message = MessageSerializer(required=False)
    channel_post = MessageSerializer(required=False)
    edited_channel_post = MessageSerializer(required=False)
    inline_query = InlineQuerySerializer(required=False)
    chosen_inline_result = ChosenInlineResultSerializer(required=False)
    callback_query = CallbackQuerySerializer(required=False)
    shipping_query = ShippingQuerySerializer(required=False)
    pre_checkout_query = PreCheckoutQuerySerializer(required=False)
    poll = PollSerializer(required=False)
    poll_answer = PollAnswerSerializer(required=False)
    my_chat_member = ChatMemberUpdatedSerializer(required=False)
    chat_member = ChatMemberUpdatedSerializer(required=False)

    def create(self, validated_data):
        update_id = validated_data.get('update_id')
        andrid = self.update_id(update_id)