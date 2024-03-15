from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
    verbose_name = _('user profile')

    def ready(self) -> None:
        from . import signals
        return super().ready()
