from django.apps import AppConfig


class ServiceVaultConfig(AppConfig):
    name = 'service_vault'

    def ready(self):
        import service_vault.signals
