from django.apps import AppConfig


class RidersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'riders'
    
    def ready(self):
        import riders.signals
