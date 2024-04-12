from django.apps import AppConfig


class ResponseConfig(AppConfig):
    """Базовый конфиг, добавление сигнала"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'response'

    def ready(self):
        import response.signals
