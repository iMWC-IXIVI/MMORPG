from django.apps import AppConfig


class UserConfig(AppConfig):
    """Базовый конфиг, включение сигналов"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals
