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
        update_id_data = validated_data.pop('update_id', None)
        message_data = validated_data.pop('message', None)
        edited_message_data = validated_data.pop('edited_message')
        channel_post_data = validated_data.pop('channel_post', None)
        edited_channel_post_data = validated_data.pop('edited_channel_post', None)
        inline_query_data = validated_data.pop('inline_query', None)
        chosen_inline_result_data = validated_data.pop('chosen_inline_result', None)
        callback_query_data = validated_data.pop('callback_query', None)
        shipping_query_data = validated_data.pop('shipping_query', None)
        pre_checkout_query_data = validated_data.pop('pre_checkout_query', None)
        poll_data = validated_data.pop('poll', None)
        poll_answer_data = validated_data.pop('poll_answer', None)
        my_chat_member_data = validated_data.pop('my_chat_member', None)
        chat_member_data = validated_data.pop('chat_member', None)
        update = Update(**validated_data)

        if update_id_data:
            update_id_ser = self.field['update_id']
            update_id = update_id_ser(**update_id_data)
            update_id = update_id.is_valid().save()
            update.update_id = update_id 
        if message_data:
            message_ser = self.field['message']
            message = message_ser(**message_data)
            message = message.is_valid().save()
            update.message = message
        if edited_message_data:
            edited_message_ser = self.field['edited_message']
            edited_message = edited_message_ser(**edited_message_data)
            edited_message = edited_message.is_valid().save()
            update.edited_message = edited_message 
        if channel_post_data:
            channel_post_ser = self.field['channel_post']
            channel_post = channel_post_ser(**channel_post_data)
            channel_post = channel_post.is_valid().save()
            update.channel_post = channel_post 
        if edited_channel_post_data:
            edited_channel_post_ser = self.field['edited_channel_post']
            edited_channel_post = edited_channel_post_ser(**edited_channel_post_data)
            edited_channel_post = edited_channel_post.is_valid().save()
            update.edited_channel_post = edited_channel_post 
        if inline_query_data:
            inline_query_ser = self.field['inline_query']
            inline_query = inline_query_ser(**inline_query_data)
            inline_query = inline_query.is_valid().save()
            update.inline_query = inline_query 
        if chosen_inline_result_data:
            chosen_inline_result_ser = self.field['chosen_inline_result']
            chosen_inline_result = chosen_inline_result_ser(**chosen_inline_result_data)
            chosen_inline_result = chosen_inline_result.is_valid().save()
            update.chosen_inline_result = chosen_inline_result 
        if callback_query_data:
            callback_query_ser = self.field['callback_query']
            callback_query = callback_query_ser(**callback_query_data)
            callback_query = callback_query.is_valid().save()
            update.callback_query = callback_query 
        if shipping_query_data:
            shipping_query_ser = self.field['shipping_query']
            shipping_query = shipping_query_ser(**shipping_query_data)
            shipping_query = shipping_query.is_valid().save()
            update.shipping_query = shipping_query 
        if pre_checkout_query_data:
            pre_checkout_query_ser = self.field['pre_checkout_query']
            pre_checkout_query = pre_checkout_query_ser(**pre_checkout_query_data)
            pre_checkout_query = pre_checkout_query.is_valid().save()
            update.pre_checkout_query = pre_checkout_query 
        if poll_data:
            poll_ser = self.field['poll']
            poll = poll_ser(**poll_data)
            poll = poll.is_valid().save()
            update.poll = poll 
        if poll_answer_data:
            poll_answer_ser = self.field['poll_answer']
            poll_answer = poll_answer_ser(**poll_answer_data)
            poll_answer = poll_answer.is_valid().save()
            update.poll_answer = poll_answer 
        if my_chat_member_data:
            my_chat_member_ser = self.field['my_chat_member']
            my_chat_member = my_chat_member_ser(**my_chat_member_data)
            my_chat_member = my_chat_member.is_valid().save()
            update.my_chat_member = my_chat_member 
        if chat_member_data:
            chat_member_ser = self.field['chat_member']
            chat_member = chat_member_ser(**chat_member_data)
            chat_member = chat_member.is_valid().save()
            update.chat_member = chat_member 
        
        return update.save()