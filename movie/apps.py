from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie'


    def ready(self):
        from .import signals