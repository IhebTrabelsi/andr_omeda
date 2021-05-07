from django.apps import AppConfig


class AndrBotConfig(AppConfig):
    name = 'andr_omeda.andr_bot'

    def ready(self):
        import andr_omeda.andr_bot.signals
