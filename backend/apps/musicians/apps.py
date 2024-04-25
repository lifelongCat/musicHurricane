from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MusiciansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.musicians'
    verbose_name = _('musicians')
