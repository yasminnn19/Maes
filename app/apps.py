from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'  # Substitua 'app' pelo nome real do seu aplicativo
    
    def ready(self):
        """
        Método executado quando o app está totalmente carregado
        Pode ser usado para configurar sinais ou outras inicializações
        """
        # Importe seus sinais aqui se estiver usando
        # from . import signals
        pass