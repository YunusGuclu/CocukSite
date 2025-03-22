from django.apps import AppConfig

class ÇocukConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Çocuk"

    def ready(self):
        from .scheduler import start
        start()