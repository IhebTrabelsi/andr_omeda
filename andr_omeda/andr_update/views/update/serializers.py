# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.views.andrid.serializers import AndridSerializer
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.message.serializers import MessageSerializer
from andr_omeda.andr_update.views.inlinequery.serializers import InlineQuerySerializer
from andr_omeda.andr_update.views.choseninlineresult.serializers import ChosenInlineResultSerializer
from andr_omeda.andr_update.views.callbackquery.serializers import CallbackQuerySerializer
from andr_omeda.andr_update.views.shippingquery.serializers import ShippingQuerySerializer
from andr_omeda.andr_update.views.precheckoutquery.serializers import PreCheckoutQuerySerializer
from andr_omeda.andr_update.views.poll.serializers import PollSerializer
from andr_omeda.andr_update.views.pollanswer.serializers import PollAnswerSerializer
from andr_omeda.andr_update.views.chatmemberupdated.serializers import ChatMemberUpdatedSerializer
from andr_omeda.andr_update.models import Update, Andrid, Message, InlineQuery, \
    ChosenInlineResult, CallbackQuery, ShippingQuery, PreCheckoutQuery, Poll, ChatMemberUpdated
import json



class UpdateSerializer(serializers.ModelSerializer):
    
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

    class Meta:
        model = Update 
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context['request']
        validated_data = request.data
        
        print("*\n"*5)
        print(validated_data)
        print("*\n"*5)
        update_id_data = validated_data.get('update_id', None)
        print(validated_data.get('message', None))
        message_data = validated_data.get('message', None)
        edited_message_data = validated_data.get('edited_message', None)
        channel_post_data = validated_data.get('channel_post', None)
        edited_channel_post_data = validated_data.get('edited_channel_post', None)
        inline_query_data = validated_data.get('inline_query', None)
        chosen_inline_result_data = validated_data.get('chosen_inline_result', None)
        callback_query_data = validated_data.get('callback_query', None)
        shipping_query_data = validated_data.get('shipping_query', None)
        pre_checkout_query_data = validated_data.get('pre_checkout_query', None)
        poll_data = validated_data.get('poll', None)
        poll_answer_data = validated_data.get('poll_answer', None)
        my_chat_member_data = validated_data.get('my_chat_member', None)
        chat_member_data = validated_data.get('chat_member', None)
        

        if update_id_data:
            update_id_ser = self.fields['update_id']
            print(update_id_data)
            update_id = AndridSerializer(data=update_id_data)
            update_id_is_valid = update_id.is_valid()
            print(update_id_is_valid)
            #update_id = update_id.save()
            print("//**"*10)
            validated_data['update_id'] = update_id
        if message_data:
            message_ser = self.fields['message']
            #print(validated_data.get('message', None)
            message = MessageSerializer(**message_data)
            message_is_valid = message.is_valid()
            message = message.save()
            validated_data['message'] = message
        if edited_message_data:
            edited_message_ser = self.fields['edited_message']
            edited_message = MessageSerializer(**edited_message_data)
            edited_message_is_valid = edited_message.is_valid()
            edited_message = edited_message.save()
            validated_data['edited_message'] = edited_message
        if channel_post_data:
            channel_post_ser = self.fields['channel_post']
            channel_post = MessageSerializer(**channel_post_data)
            channel_post_is_valid = channel_post.is_valid()
            channel_post = channel_post.save()
            validated_data['channel_post'] = channel_post
        if edited_channel_post_data:
            edited_channel_post_ser = self.fields['edited_channel_post']
            edited_channel_post = MessageSerializer(**edited_channel_post_data)
            edited_channel_post_is_valid = edited_channel_post.is_valid()
            edited_channel_post = edited_channel_post.save()
            validated_data['edited_channel_post'] = edited_channel_post 
        if inline_query_data:
            inline_query_ser = self.fields['inline_query']
            inline_query = InlineQuerySerializer(**inline_query_data)
            inline_query_is_valid = inline_query.is_valid()
            inline_query = inline_query.save()
            validated_data['inline_query'] = inline_query 
        if chosen_inline_result_data:
            chosen_inline_result_ser = self.fields['chosen_inline_result']
            chosen_inline_result = ChosenInlineResultSerializer(**chosen_inline_result_data)
            chosen_inline_result_is_valid = chosen_inline_result.is_valid()
            chosen_inline_result = chosen_inline_result.save()
            validated_data['chosen_inline_result'] = chosen_inline_result 
        if callback_query_data:
            callback_query_ser = self.fields['callback_query']
            callback_query = CallbackQuerySerializer(**callback_query_data)
            callback_query_is_valid = callback_query.is_valid()
            callback_query = callback_query.save()
            validated_data['callback_query'] = callback_query 
        if shipping_query_data:
            shipping_query_ser = self.fields['shipping_query']
            shipping_query = ShippingQuerySerializer(**shipping_query_data)
            shipping_query_is_valid = shipping_query.is_valid()
            shipping_query = shipping_query.save()
            validated_data['shipping_query'] = shipping_query 
        if pre_checkout_query_data:
            pre_checkout_query_ser = self.fields['pre_checkout_query']
            pre_checkout_query = PreCheckoutQuerySerializer(**pre_checkout_query_data)
            pre_checkout_query_is_valid = pre_checkout_query.is_valid()
            pre_checkout_query = pre_checkout_query.save()
            validated_data['pre_checkout_query'] = pre_checkout_query 
        if poll_data:
            poll_ser = self.fields['poll']
            poll = PollSerializer(**poll_data)
            poll_is_valid = poll.is_valid()
            poll = poll.save()
            validated_data['poll'] = poll  
        if poll_answer_data:
            poll_answer_ser = self.fields['poll_answer']
            poll_answer = PollAnswerSerializer(**poll_answer_data)
            poll_answer_is_valid = poll_answer.is_valid()
            poll_answer = poll_answer.save()
            validated_data['poll_answer'] = poll_answer 
        if my_chat_member_data:
            my_chat_member_ser = self.fields['my_chat_member']
            my_chat_member = ChatMemberUpdatedSerializer(**my_chat_member_data)
            my_chat_member_is_valid = my_chat_member.is_valid()
            my_chat_member = my_chat_member.save()
            validated_data['my_chat_member'] = my_chat_member 
        if chat_member_data:
            chat_member_ser = self.fields['chat_member']
            chat_member = ChatMemberUpdatedSerializer(**chat_member_data)
            chat_member_is_valid = chat_member.is_valid()
            chat_member = chat_member.save()
            validated_data['chat_member'] = chat_member 
        print("?**"*10)
        print(validated_data)
        update = Update(**validated_data)
        return update.save()