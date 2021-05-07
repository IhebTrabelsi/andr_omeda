from django.core.management.base import BaseCommand
from andr_omeda.andr_bot.helpers import set_webhook_for_bot_with_token, \
    update_webhook_fields_for_bot_with_token


class Command(BaseCommand):
    help = 'webhook must be reset every time ngrok reruns'

    def add_arguments(self, parser):
        parser.add_argument('domain', type=str, help='Example: 6d215154ca47.ngrok.io')
        parser.add_argument('token', type=str, help='Example: 1752852391:AAGCvJMMtvwamcq7fKWoz1ovi_MsPYrP7Kg')

    def handle(self, *args, **kwargs):
        domain = kwargs['domain']
        token = kwargs['token']

        res = set_webhook_for_bot_with_token(
            domain=domain,
            token=token
        )

        update_webhook_fields_for_bot_with_token(token=token, request_res=res)
