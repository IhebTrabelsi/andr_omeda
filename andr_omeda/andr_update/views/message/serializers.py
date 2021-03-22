# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Message
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.location.serializers import LocationSerializer
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer
from andr_omeda.andr_update.views.audio.serializers import AudioSerializer
from andr_omeda.andr_update.views.contact.serializers import ContactSerializer
from andr_omeda.andr_update.views.dice.serializers import DiceSerializer
from andr_omeda.andr_update.views.document.serializers import DocumentSerializer
from andr_omeda.andr_update.views.game.serializers import GameSerializer
from andr_omeda.andr_update.views.inlinekeyboardmarkup.serializers import InlineKeyboardMarkupSerializer
from andr_omeda.andr_update.views.invoice.serializers import InvoiceSerializer
from andr_omeda.andr_update.views.passportdata.serializers import PassportDataSerializer
from andr_omeda.andr_update.views.poll.serializers import PollSerializer
from andr_omeda.andr_update.views.proximityalerttriggered.serializers import ProximityAlertTriggeredSerializer
from andr_omeda.andr_update.views.sticker.serializers import StickerSerializer
from andr_omeda.andr_update.views.successfulpayment.serializers import SuccessfulPaymentSerializer
from andr_omeda.andr_update.views.venue.serializers import VenueSerializer
from andr_omeda.andr_update.views.video.serializers import VideoSerializer
from andr_omeda.andr_update.views.videonote.serializers import VideoNoteSerializer
from andr_omeda.andr_update.views.voice.serializers import VoiceSerializer
from andr_omeda.andr_update.views.voicechatended.serializers import VoiceChatEndedSerializer
from andr_omeda.andr_update.views.voicechatstarted.serializers import VoiceChatStartedSerializer
from andr_omeda.andr_update.views.voicechatparticipantsinvited.serializers import VoiceChatParticipantsInvitedSerializer
from andr_omeda.andr_update.views.messageautodeletetimerchanged.serializers import MessageAutoDeleteTimerChangedSerializer

from rest_framework import serializers
from andr_omeda.andr_update.models import Chat
from andr_omeda.andr_update.views.chatlocation.serializers import ChatLocationSerializer
from andr_omeda.andr_update.views.chatpermissions.serializers import ChatPermissionsSerializer
from andr_omeda.andr_update.views.chatphoto.serializers import ChatPhotoSerializer
from andr_omeda.andr_update.views.animation.serializers import AnimationSerializer


class ChatSerializer(serializers.ModelSerializer):
    location = ChatLocationSerializer(required=False)
    permissions = ChatPermissionsSerializer(required=False)
    photo = ChatPhotoSerializer(required=False)
    
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        chat_id = validated_data.get('id')
        if Chat.chat_with_id_exists(chat_id=chat_id):
            return Chat.objects.get(pk=chat_id)

        loc_ser = self.fields['location']
        perm_ser = self.fields['permissions']
        photo_ser = self.fields['photo']
        pinned_message_ser = self.fields['pinned_message']

        if validated_data.get('location'):
            loc = ChatLocationSerializer(**validated_data.pop('location', None))
            loc = loc.is_valid()
            loc = loc.save()
            validated_data['location'] = loc

        if validated_data.get('permissions'):
            perm = ChatPermissionsSerializer(**validated_data.pop('permissions', None))
            perm = perm.is_valid()
            perm = perm.save()
            validated_data['permissions'] = perm

        if validated_data.get('photo'):
            photo = ChatPhotoSerializer(**validated_data.pop('permissions', None))
            photo = photo.is_valid()
            photo = photo.save()
            validated_data['photo'] = photo

        
        chat = Chat(**validated_data)
        chat.save()
        return chat

class MessageSerializer(serializers.ModelSerializer):
    message_from = AndruserSerializer(required=False)
    forward_from = AndruserSerializer(required=False)
    via_bot = AndruserSerializer(required=False)
    user = AndruserSerializer(required=False)
    chat = ChatSerializer()
    sender_chat = ChatSerializer(required=False)
    forward_from_chat = ChatSerializer(required=False)
    new_chat_members = AndruserSerializer(many=True, required=False)
    left_chat_member = AndruserSerializer(required=False)
    animation = AnimationSerializer(required=False)
    location = LocationSerializer(required=False)
    entities = MessageEntitySerializer(many=True, required=False)
    caption_entities = MessageEntitySerializer(many=True, required=False)
    photo = PhotoSizeSerializer(many=True, required=False)
    new_chat_photo = PhotoSizeSerializer(many=True, required=False)
    audio = AudioSerializer(required=False)
    contact = ContactSerializer(required=False)
    dice = DiceSerializer(required=False)
    document = DocumentSerializer(required=False)
    game = GameSerializer(required=False)
    reply_markup = InlineKeyboardMarkupSerializer(required=False)
    invoice = InvoiceSerializer(required=False)
    passport_data = PassportDataSerializer(required=False)
    poll = PollSerializer(required=False)
    proximity_alert_triggered = ProximityAlertTriggeredSerializer(required=False)
    sticker = StickerSerializer(required=False)
    successful_payment = SuccessfulPaymentSerializer(required=False)
    venue = VenueSerializer(required=False)
    video = VideoSerializer(required=False)
    video_note = VideoNoteSerializer(required=False)
    voice = VoiceSerializer(required=False)
    voice_chat_ended = VoiceChatEndedSerializer(required=False)
    voice_chat_started = VoiceChatStartedSerializer(required=False)
    voice_chat_participants_invited = VoiceChatParticipantsInvitedSerializer(required=False)

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('from', None)
        sender_chat_data = validated_data.pop('sender_chat', None)
        chat_data = validated_data.pop('chat')
        forward_from_data = validated_data.pop('forward_from', None)
        forward_from_chat_data = validated_data.pop('forward_from_chat', None)
        reply_to_message_data = validated_data.pop('reply_to_message', None)
        via_bot_data = validated_data.pop('via_bot', None)
        entities_data = validated_data.pop('entities', None)
        animation_data = validated_data.pop('animation', None)
        audio_data = validated_data.pop('audio', None)
        document_data = validated_data.pop('document', None)
        photo_data = validated_data.pop('photo', None)
        sticker_data = validated_data.pop('sticker', None)
        video_data = validated_data.pop('video', None)
        video_note_data = validated_data.pop('video_note', None)
        voice_data = validated_data.pop('voice', None)
        caption_entities_data = validated_data.pop('caption_entities', None)
        contact_data = validated_data.pop('contact', None)
        dice_data = validated_data.pop('dice', None)
        game_data = validated_data.pop('game', None)
        poll_data = validated_data.pop('poll', None)
        venue_data = validated_data.pop('venue', None)
        location_data = validated_data.pop('location', None)
        new_chat_members_data = validated_data.pop('new_chat_members', None)
        left_chat_member_data = validated_data.pop('left_chat_member', None)
        new_chat_photo_data = validated_data.pop('new_chat_photo', None)
        #TODO [workaround] to be implemented later
        message_auto_delete_timer_changed_data = validated_data.pop('poll', None)
        pinned_message_data = validated_data.pop('pinned_message', None)
        invoice_data = validated_data.pop('invoice', None)
        successful_payment_data = validated_data.pop('successful_payment', None)
        passport_data_data = validated_data.pop('passport_data', None)
        proximity_alert_triggered_data = validated_data.pop('proximity_alert_triggered', None)
        #TODO [workaround] currently holds no information
        voice_chat_started_data = validated_data.pop('voice_chat_started', None)
        voice_chat_ended_data = validated_data.pop('voice_chat_ended', None)
        voice_chat_participants_invited_data = validated_data.pop('voice_chat_participants_invited', None)
        reply_markup_data = validated_data.pop('reply_markup', None)
        print("?"*10)

        if user_data:
            message_from = AndruserSerializer(**user_data)
            message_from = message_from.is_valid()
            message_from = message_from.save()
            validated_data['message_from'] = message_from
        if sender_chat_data:
            sender_chat = ChatSerializer(**sender_chat_data)
            sender_chat = sender_chat.is_valid()
            sender_chat = sender_chat.save()
            validated_data['sender_chat'] = sender_chat
        if chat_data:
            chat = ChatSerializer(**chat_data)
            print("?"*10)
            print(chat.is_valid())
            print("-"*10)
            print()
            chat = chat.is_valid()
            chat = chat.save()
            validated_data['chat'] = chat
        if forward_from_data:
            forward_from = AndruserSerializer(**forward_from_data)
            forward_from = forward_from.is_valid()
            forward_from = forward_from.save()
            validated_data['forward_from'] = forward_from
        if forward_from_chat_data:
            forward_from_chat = ChatSerializer(**forward_from_chat_data)
            forward_from_chat = forward_from_chat.is_valid()
            forward_from_chat = forward_from_chat.save()
            validated_data['forward_from_chat'] = forward_from_chat 
        if via_bot_data:
            via_bot = AndruserSerializer(**via_bot_data)
            via_bot = via_bot.is_valid()
            via_bot = via_bot.save()
            validated_data['via_bot'] = via_bot  
        if sender_chat_data:
            sender_chat = ChatSerializer(**sender_chat_data)
            sender_chat = sender_chat.is_valid()
            sender_chat = sender_chat.save()
            validated_data['sender_chat'] = sender_chat 
        if entities_data:
            entities = MessageEntitySerializer(**chat_data)
            entities = entities.is_valid()
            entities = entities.save()
            validated_data['entities'] = entities 
        if animation_data:
            animation = AnimationSerializer(**animation_data)
            animation = animation.is_valid()
            animation = animation.save()
            validated_data['animation'] = animation 
        if audio_data:
            audio = AudioSerializer(**audio_data)
            audio = audio.is_valid()
            audio = audio.save()
            validated_data['audio'] = audio
        if document_data:
            document = DocumentSerializer(**document_data)
            document = document.is_valid()
            document = document.save()
            validated_data['document'] = document
        if photo_data:
            photo = PhotoSizeSerializer(**photo_data)
            photo = photo.is_valid()
            photo = photo.save()
            validated_data['photo'] = photo 
        if sticker_data:
            sticker = StickerSerializer(**sticker_data)
            sticker = sticker.is_valid()
            sticker = sticker.save()
            validated_data['sticker'] = sticker  
        if video_data:
            video = VideoSerializer(**video_data)
            video = video.is_valid()
            video = video.save()
            validated_data['video'] = video 
        if video_note_data:
            video_note = VideoNoteSerializer(**video_note_data)
            video_note = video_note.is_valid()
            video_note = video_note.save()
            validated_data['video_note'] = video_note 
        if voice_data:
            voice = VoiceSerializer(**voice_data)
            voice = voice.is_valid()
            voice = voice.save()
            validated_data['voice'] = voice 
        if caption_entities_data:
            caption_entities = MessageEntitySerializer(**caption_entities_data)
            caption_entities = caption_entities.is_valid()
            caption_entities = caption_entities.save()
            validated_data['caption_entities'] = caption_entities 
        if contact_data:
            contact = ContactSerializer(**contact_data)
            contact = contact.is_valid()
            contact = contact.save()
            validated_data['contact'] = contact 
        if dice_data:
            dice = DiceSerializer(**dice_data)
            dice = dice.is_valid()
            dice = dice.save()
            validated_data['dice'] = dice 
        if game_data:
            game = GameSerializer(**game_data)
            game = game.is_valid()
            game = game.save()
            validated_data['game'] = game 
        if poll_data:
            poll = PollSerializer(**poll_data)
            poll = poll.is_valid()
            poll = poll.save()
            validated_data['poll'] = poll 
        if venue_data:
            venue = VenueSerializer(**venue_data)
            venue = venue.is_valid()
            venue = venue.save()
            validated_data['venue'] = venue 
        if location_data:
            location = LocationSerializer(**location_data)
            location = location.is_valid()
            location = location.save()
            validated_data['location'] = location 
        if new_chat_members_data:
            new_chat_members = AndruserSerializer(**new_chat_members_data)
            new_chat_members = new_chat_members.is_valid()
            new_chat_members = new_chat_members.save()
            validated_data['new_chat_members'] = new_chat_members 
        if left_chat_member_data:
            left_chat_member = AndruserSerializer(**left_chat_member_data)
            left_chat_member = left_chat_member.is_valid()
            left_chat_member = left_chat_member.save()
            validated_data['left_chat_member'] = left_chat_member 
        if new_chat_photo_data:
            new_chat_photo = PhotoSizeSerializer(**new_chat_photo_data)
            new_chat_photo = new_chat_photo.is_valid()
            new_chat_photo = new_chat_photo.save()
            validated_data['new_chat_photo'] = new_chat_photo  
        if message_auto_delete_timer_changed_data:
            message_auto_delete_timer_changed = MessageAutoDeleteTimerChangedSerializer(**message_auto_delete_timer_changed_data)
            message_auto_delete_timer_changed = message_auto_delete_timer_changed.is_valid()
            message_auto_delete_timer_changed = message_auto_delete_timer_changed.save()
            validated_data['message_auto_delete_timer_changed'] = message_auto_delete_timer_changed  
        if invoice_data:
            invoice = InvoiceSerializer(**invoice_data)
            invoice = invoice.is_valid()
            invoice = invoice.save()
            validated_data['invoice'] = invoice  
        if successful_payment_data:
            successful_payment = SuccessfulPaymentSerializer(**successful_payment_data)
            successful_payment = successful_payment.is_valid()
            successful_payment = successful_payment.save()
            validated_data['successful_payment'] = successful_payment  
        if passport_data_data:
            passport_data = PassportDataSerializer(**passport_data_data)
            passport_data = passport_data.is_valid()
            passport_data = passport_data.save()
            validated_data['passport_data'] = passport_data  
        if proximity_alert_triggered_data:
            proximity_alert_triggered = ProximityAlertTriggeredSerializer(**proximity_alert_triggered_data)
            proximity_alert_triggered = proximity_alert_triggered.is_valid()
            proximity_alert_triggered = proximity_alert_triggered.save()
            validated_data['proximity_alert_triggered'] = proximity_alert_triggered 
        if voice_chat_started_data:
            voice_chat_started = VoiceChatStartedSerializer(**voice_chat_started_data)
            voice_chat_started = voice_chat_started.is_valid()
            voice_chat_started = voice_chat_started.save()
            validated_data['voice_chat_started'] = voice_chat_started  
        if voice_chat_ended_data:
            voice_chat_ended = VoiceChatEndedSerializer(**voice_chat_ended_data)
            voice_chat_ended = voice_chat_ended.is_valid()
            voice_chat_ended = voice_chat_ended.save()
            validated_data['voice_chat_ended'] = voice_chat_ended   
        if voice_chat_participants_invited_data:
            voice_chat_participants_invited = VoiceChatParticipantsInvitedSerializer(**voice_chat_participants_invited_data)
            voice_chat_participants_invited = voice_chat_participants_invited.is_valid()
            voice_chat_participants_invited = voice_chat_participants_invited.save()
            validated_data['voice_chat_participants_invited'] = voice_chat_participants_invited  
        if reply_markup_data:
            reply_markup = InlineKeyboardMarkupSerializer(**reply_markup_data)
            reply_markup = reply_markup.is_valid()
            reply_markup = reply_markup.save()
            validated_data['reply_markup'] = reply_markup 
        message = Message(**validated_data)
        return message.save()
        
        

    

