from django.apps import AppConfig


class ActividadesDeUsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actividades_de_usuario'

    def ready(self):
        import actividades_de_usuario.signals  