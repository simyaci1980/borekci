from django.apps import AppConfig


class AnaSayfaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ana_sayfa'
    
    def ready(self):
        """Uygulama hazır olduğunda signals'ı yükle"""
        import ana_sayfa.signals
