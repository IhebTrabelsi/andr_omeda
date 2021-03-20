# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Message
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.location.serializers import LocationSerializer
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer
from andr_omeda.andr_update.views.audio.serializers import AudioSerializer
from andr_omeda.andr_update.views.chat.serializers import ChatSerializer
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

class MessageSerializer(serializers.ModelSerializer):
    message_from = AndruserSerializer()
    forward_from = AndruserSerializer()
    via_bot = AndruserSerializer()
    user = AndruserSerializer()
    new_chat_members = AndruserSerializer(many=True)
    left_chat_member = AndruserSerializer()
    animation = AnimationSerializer()
    location = LocationSerializer()
    entities = MessageEntitySerializer(many=True)
    caption_entities = MessageEntitySerializer(many=True)
    photo = PhotoSizeSerializer(many=True)
    new_chat_photo = PhotoSizeSerializer(many=True)
    audio = AudioSerializer()
    chat = ChatSerializer()
    sender_chat = ChatSerializer()
    forward_from_chat = ChatSerializer()
    contact = ContactSerializer()
    dice = DiceSerializer()
    document = DocumentSerializer()
    game = GameSerializer()
    reply_markup = InlineKeyboardMarkupSerializer()
    invoice = InvoiceSerializer()
    passport_data = PassportDataSerializer()
    poll = PollSerializer()
    proximity_alert_triggered = ProximityAlertTriggeredSerializer()
    sticker = StickerSerializer()
    successful_payment = SuccessfulPaymentSerializer()
    venue = VenueSerializer()
    video = VideoSerializer()
    video_note = VideoNoteSerializer()
    voice = VoiceSerializer()
    voice_chat_ended = VoiceChatEndedSerializer()
    voice_chat_started = VoiceChatStartedSerializer()
    voice_chat_participants_invited = VoiceChatParticipantsInvitedSerializer()

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

        message = Message(**validated_data)

        if user_data:
            user_ser = self.field['message_from']
            message_from = user_ser(**user_data)
            message_from = message_from.is_valid().save()
            message.message_from = message_from 
        if sender_chat_data:
            sender_chat_ser = self.field['sender_chat']
            sender_chat = sender_chat_ser(**sender_chat_data)
            sender_chat = sender_chat.is_valid().save()
            message.sender_chat = sender_chat
        if chat_data:
            chat_ser = self.field['chat']
            chat = chat_ser(**chat_data)
            chat = chat.is_valid().save()
            message.chat = chat 
        if forward_from_data:
            forward_from_ser = self.field['forward_from']
            forward_from = forward_from_ser(**forward_from_data)
            forward_from = forward_from.is_valid().save()
            message.forward_from = forward_from 
        if forward_from_chat_data:
            forward_from_chat_ser = self.field['forward_from_chat']
            forward_from_chat = forward_from_chat_ser(**forward_from_chat_data)
            forward_from_chat = forward_from_chat.is_valid().save()
            message.forward_from_chat = forward_from_chat 
        if via_bot_data:
            via_bot_ser = self.field['via_bot']
            via_bot = via_bot_ser(**via_bot_data)
            via_bot = via_bot.is_valid().save()
            message.via_bot = via_bot 
        if sender_chat_data:
            sender_chat_ser = self.field['sender_chat']
            sender_chat = sender_chat_ser(**sender_chat_data)
            sender_chat = sender_chat.is_valid().save()
            message.sender_chat = sender_chat
        if entities_data:
            entities_ser = self.field['entities']
            entities = entities_ser(**chat_data)
            entities = entities.is_valid().save()
            message.entities = entities 
        if animation_data:
            animation_ser = self.field['animation']
            animation = animation_ser(**animation_data)
            animation = animation.is_valid().save()
            message.animation = animation 
        if audio_data:
            audio_ser = self.field['audio']
            audio = audio_ser(**audio_data)
            audio = audio.is_valid().save()
            message.audio = audio 
        if document_data:
            document_ser = self.field['document']
            document = document_ser(**document_data)
            document = document.is_valid().save()
            message.document = document 
        if photo_data:
            photo_ser = self.field['photo']
            photo = photo_ser(**photo_data)
            photo = photo.is_valid().save()
            message.photo = photo 
        if sticker_data:
            sticker_ser = self.field['sticker']
            sticker = sticker_ser(**sticker_data)
            sticker = sticker.is_valid().save()
            message.sticker = sticker 
        if video_data:
            video_ser = self.field['video']
            video = video_ser(**video_data)
            video = video.is_valid().save()
            message.video = video 
        if video_note_data:
            video_note_ser = self.field['video_note']
            video_note = video_note_ser(**video_note_data)
            video_note = video_note.is_valid().save()
            message.video_note = video_note 
        if voice_data:
            voice_ser = self.field['voice']
            voice = voice_ser(**voice_data)
            voice = voice.is_valid().save()
            message.voice = voice 
        if caption_entities_data:
            caption_entities_ser = self.field['caption_entities']
            caption_entities = caption_entities_ser(**caption_entities_data)
            caption_entities = caption_entities.is_valid().save()
            message.caption_entities = caption_entities 
        if contact_data:
            contact_ser = self.field['contact']
            contact = contact_ser(**contact_data)
            contact = contact.is_valid().save()
            message.contact = contact 
        if dice_data:
            dice_ser = self.field['dice']
            dice = dice_ser(**dice_data)
            dice = dice.is_valid().save()
            message.dice = dice 
        if game_data:
            game_ser = self.field['game']
            game = game_ser(**game_data)
            game = game.is_valid().save()
            message.game = game 
        if poll_data:
            poll_ser = self.field['poll']
            poll = poll_ser(**poll_data)
            poll = poll.is_valid().save()
            message.poll = poll 
        if venue_data:
            venue_ser = self.field['venue']
            venue = venue_ser(**venue_data)
            venue = venue.is_valid().save()
            message.venue = venue 
        if location_data:
            location_ser = self.field['location']
            location = location_ser(**location_data)
            location = location.is_valid().save()
            message.location = location 
        if new_chat_members_data:
            new_chat_members_ser = self.field['new_chat_members']
            new_chat_members = new_chat_members_ser(**new_chat_members_data)
            new_chat_members = new_chat_members.is_valid().save()
            message.new_chat_members = new_chat_members 
        if left_chat_member_data:
            left_chat_member_ser = self.field['left_chat_member']
            left_chat_member = left_chat_member_ser(**left_chat_member_data)
            left_chat_member = left_chat_member.is_valid().save()
            message.left_chat_member = left_chat_member 
        if new_chat_photo_data:
            new_chat_photo_ser = self.field['new_chat_photo']
            new_chat_photo = new_chat_photo_ser(**new_chat_photo_data)
            new_chat_photo = new_chat_photo.is_valid().save()
            message.new_chat_photo = new_chat_photo 
        if message_auto_delete_timer_changed_data:
            message_auto_delete_timer_changed_ser = self.field['message_auto_delete_timer_changed']
            message_auto_delete_timer_changed = message_auto_delete_timer_changed_ser(**message_auto_delete_timer_changed_data)
            message_auto_delete_timer_changed = message_auto_delete_timer_changed.is_valid().save()
            message.message_auto_delete_timer_changed = message_auto_delete_timer_changed 
        if pinned_message_data:
            pinned_message_ser = self.field['pinned_message']
            pinned_message = pinned_message_ser(**pinned_message_data)
            pinned_message = pinned_message.is_valid().save()
            message.pinned_message = pinned_message 
        if invoice_data:
            invoice_ser = self.field['invoice']
            invoice = invoice_ser(**invoice_data)
            invoice = invoice.is_valid().save()
            message.invoice = invoice  
        if successful_payment_data:
            successful_payment_ser = self.field['successful_payment']
            successful_payment = successful_payment_ser(**successful_payment_data)
            successful_payment = successful_payment.is_valid().save()
            message.successful_payment = successful_payment 
        if passport_data_data:
            passport_data_ser = self.field['passport_data']
            passport_data = passport_data_ser(**passport_data_data)
            passport_data = passport_data.is_valid().save()
            message.passport_data = passport_data 
        if proximity_alert_triggered_data:
            proximity_alert_triggered_ser = self.field['proximity_alert_triggered']
            proximity_alert_triggered = proximity_alert_triggered_ser(**proximity_alert_triggered_data)
            proximity_alert_triggered = proximity_alert_triggered.is_valid().save()
            message.proximity_alert_triggered = proximity_alert_triggered 
        if voice_chat_started_data:
            voice_chat_started_ser = self.field['voice_chat_started']
            voice_chat_started = voice_chat_started_ser(**voice_chat_started_data)
            voice_chat_started = voice_chat_started.is_valid().save()
            message.voice_chat_started = voice_chat_started 
        if voice_chat_ended_data:
            voice_chat_ended_ser = self.field['voice_chat_ended']
            voice_chat_ended = voice_chat_ended_ser(**voice_chat_ended_data)
            voice_chat_ended = voice_chat_ended.is_valid().save()
            message.voice_chat_ended = voice_chat_ended 
        if voice_chat_participants_invited_data:
            voice_chat_participants_invited_ser = self.field['voice_chat_participants_invited']
            voice_chat_participants_invited = voice_chat_participants_invited_ser(**voice_chat_participants_invited_data)
            voice_chat_participants_invited = voice_chat_participants_invited.is_valid().save()
            message.voice_chat_participants_invited = voice_chat_participants_invited 
        if reply_markup_data:
            reply_markup_ser = self.field['reply_markup']
            reply_markup = reply_markup_ser(**reply_markup_data)
            reply_markup = reply_markup.is_valid().save()
            message.reply_markup = reply_markup 

        return message.save()
        
        

    

