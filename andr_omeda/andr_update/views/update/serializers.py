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
    ChosenInlineResult, CallbackQuery, ShippingQuery, PreCheckoutQuery, Poll, ChatMemberUpdated, \
        Chat
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
        validated_data = self.context['validated_data']
        _unicity = self.context['unicity']
        _lists = self.context['lists']
        _specials = self.context['specials']

        update_id_data = validated_data.pop('update_id', None)
        message_data = validated_data.pop('message', None)
        edited_message_data = validated_data.pop('edited_message', None)
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


        if update_id_data != None:
            update_id = AndridSerializer(data=update_id_data)
            update_id_is_valid = update_id.is_valid(raise_exception=True)
            update_id = update_id.create(update_id.validated_data)
            validated_data['update_id'] = update_id

        if message_data:
            context = {'validated_data': message_data, 'unicity': _unicity, 'unicity_prefix': 'message', 'lists': _lists, 'specials': _specials}
            if self.context.get('message__reply_to_message', None):
                context['message__reply_to_message'] = self.context.get('message__reply_to_message')
            message = MessageSerializer(data=message_data, context=context)
            message_is_valid = message.is_valid(raise_exception=True)
            message = message.save()
            validated_data['message'] = message
        
        if  edited_message_data != None:
            context = {'validated_data': edited_message_data, 'unicity': _unicity, 'unicity_prefix': 'edited_message', 'lists': _lists, 'specials': _specials}
            if self.context.get('edited_message__reply_to_message', None):
                context['edited_message__reply_to_message'] = self.context.get('edited_message__reply_to_message')
            edited_message = MessageSerializer(data=edited_message_data, context=context)
            edited_message_is_valid = edited_message.is_valid(raise_exception=True)
            edited_message = edited_message.save()
            validated_data['edited_message'] = edited_message

        if  channel_post_data != None:
            context = {'validated_data': channel_post_data, 'unicity': _unicity, 'unicity_prefix': 'channel_post', 'lists': _lists, 'specials': _specials}
            if self.context.get('channel_post__reply_to_message', None):
                context['channel_post__reply_to_message'] = self.context.get('channel_post__reply_to_message')
            channel_post = MessageSerializer(data=channel_post_data, context=context)
            channel_post_is_valid = channel_post.is_valid(raise_exception=True)
            channel_post = channel_post.save()
            validated_data['channel_post'] = channel_post

        if  edited_channel_post_data != None:
            context = {'validated_data': edited_channel_post_data, 'unicity': _unicity, 'unicity_prefix': 'edited_channel_post', 'lists': _lists, 'specials': _specials}
            if self.context.get('edited_channel_post__reply_to_message', None):
                context['edited_channel_post__reply_to_message'] = self.context.get('edited_channel_post__reply_to_message')
            edited_channel_post = MessageSerializer(data=edited_channel_post_data, context=context)
            edited_channel_post_is_valid = edited_channel_post.is_valid(raise_exception=True)
            edited_channel_post = edited_channel_post.save()
            validated_data['edited_channel_post'] = edited_channel_post

        if  inline_query_data != None:
            context = {'validated_data': inline_query_data, 'unicity': _unicity, 'unicity_prefix': 'inline_query', 'lists': _lists}
            inline_query = InlineQuerySerializer(data=inline_query_data, context=context)
            inline_query_is_valid = inline_query.is_valid(raise_exception=True)
            inline_query = inline_query.save()
            validated_data['inline_query'] = inline_query

        if  chosen_inline_result_data != None:
            context = {'validated_data': chosen_inline_result_data, 'unicity': _unicity, 'unicity_prefix': 'chosen_inline_result', 'lists': _lists}
            chosen_inline_result = ChosenInlineResultSerializer(data=chosen_inline_result_data, context=context)
            chosen_inline_result_is_valid = chosen_inline_result.is_valid(raise_exception=True)
            chosen_inline_result = chosen_inline_result.save()
            validated_data['chosen_inline_result'] = chosen_inline_result

        if  callback_query_data != None:
            context = {'validated_data': callback_query_data, 'unicity': _unicity, 'unicity_prefix': 'callback_query', 'lists': _lists}
            callback_query = CallbackQuerySerializer(data=callback_query_data, context=context)
            callback_query_is_valid = callback_query.is_valid(raise_exception=True)
            callback_query = callback_query.save()
            validated_data['callback_query'] = callback_query

        if  shipping_query_data != None:
            context = {'validated_data': shipping_query_data, 'unicity': _unicity, 'unicity_prefix': 'shipping_query', 'lists': _lists}
            shipping_query = ShippingQuerySerializer(data=shipping_query_data, context=context)
            shipping_query_is_valid = shipping_query.is_valid(raise_exception=True)
            shipping_query = shipping_query.save()
            validated_data['shipping_query'] = shipping_query

        if  pre_checkout_query_data != None:
            context = {'validated_data': pre_checkout_query_data, 'unicity': _unicity, 'unicity_prefix': 'pre_checkout_query', 'lists': _lists}
            pre_checkout_query = PreCheckoutQuerySerializer(data=pre_checkout_query_data, context=context)
            pre_checkout_query_is_valid = pre_checkout_query.is_valid(raise_exception=True)
            pre_checkout_query = pre_checkout_query.save()
            validated_data['pre_checkout_query'] = pre_checkout_query

        if  poll_data != None:
            context = {'validated_data': poll_data, 'lists': _lists}
            poll = PollSerializer(data=poll_data, context=context)
            poll_is_valid = poll.is_valid(raise_exception=True)
            poll = poll.save()
            validated_data['poll'] = poll

        if  poll_answer_data != None:
            context = {'validated_data': poll_answer_data, 'unicity': _unicity, 'unicity_prefix': 'poll_answer', 'lists': _lists}
            poll_answer = PollAnswerSerializer(data=poll_answer_data, context=context)
            poll_answer_is_valid = poll_answer.is_valid(raise_exception=True)
            poll_answer = poll_answer.save()
            validated_data['poll_answer'] = poll_answer

        if  my_chat_member_data != None:
            context = {'validated_data': my_chat_member_data, 'unicity': _unicity, 'unicity_prefix': 'my_chat_member', 'lists': _lists}
            my_chat_member = ChatMemberUpdatedSerializer(data=my_chat_member_data, context=context)
            my_chat_member_is_valid = my_chat_member.is_valid(raise_exception=True)
            my_chat_member = my_chat_member.save()

        if  chat_member_data != None:
            chat_member = ChatMemberUpdatedSerializer(data=chat_member_data)
            chat_member_is_valid = chat_member.is_valid(raise_exception=True)
            chat_member = chat_member.save()
            validated_data['chat_member'] = chat_member

        update = Update.objects.create(**validated_data)
        
        if  my_chat_member_data:
            my_chat_member.update = update 
            my_chat_member.save()

        return update
