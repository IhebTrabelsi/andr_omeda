# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Message
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()
from andr_omeda.andr_update.views.messageentity.serializers import MessageEntitySerializer()
from andr_omeda.andr_update.views.photosize.serializers import PhotoSizeSerializer()
from andr_omeda.andr_update.views.audio.serializers import AudioSerializer()
from andr_omeda.andr_update.views.chat.serializers import ChatSerializer()
from andr_omeda.andr_update.views.contact.serializers import ContactSerializer()
from andr_omeda.andr_update.views.dice.serializers import DiceSerializer()
from andr_omeda.andr_update.views.document.serializers import DocumentSerializer()
from andr_omeda.andr_update.views.game.serializers import GameSerializer()
from andr_omeda.andr_update.views.inlinekeyboardmarkup.serializers import InlineKeyboardMarkupSerializer()
from andr_omeda.andr_update.views.invoice.serializers import InvoiceSerializer()
from andr_omeda.andr_update.views.passportdata.serializers import PassportDataSerializer()
from andr_omeda.andr_update.views.poll.serializers import PollSerializer()
from andr_omeda.andr_update.views.proximityalerttriggered.serializers import ProximityAlertTriggeredSerializer()
from andr_omeda.andr_update.views.sticker.serializers import StickerSerializer()
from andr_omeda.andr_update.views.successfulpayment.serializers import SuccessfulPaymentSerializer()
from andr_omeda.andr_update.views.venue.serializers import VenueSerializer()
from andr_omeda.andr_update.views.video.serializers import VideoSerializer()
from andr_omeda.andr_update.views.videonote.serializers import VideoNoteSerializer()
from andr_omeda.andr_update.views.voice.serializers import VoiceSerializer()


class MessageSerializer(serializers.ModelSerializer):
    message_from = AndruserSerializer()
    forward_from = AndruserSerializer()
    via_bot = AndruserSerializer()
    user = AndruserSerializer()
    new_chat_members = AndruserSerializer()
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

    class Meta:
        model = Message
        fields = '__all__'
    

