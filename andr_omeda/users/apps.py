from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "andr_omeda.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import andr_omeda.users.signals  # noqa F401
        except ImportError:
            pass
