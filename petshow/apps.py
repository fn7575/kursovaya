from django.apps import AppConfig

class PetshowConfig(AppConfig):
    name = 'petshow'

    def ready(self):
        import petshow.signals