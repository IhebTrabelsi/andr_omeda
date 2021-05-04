from rest_framework.exceptions import ValidationError
from andr_omeda.andr_bot.models.bot import Bot


def bot_already_exists(token):
    if Bot.objects.filter(token=token).exists():
        raise ValidationError


def bot_with_token_exists(token):
    if not Bot.objects.filter(token=token).exists():
        raise ValidationError
