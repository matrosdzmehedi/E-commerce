from django.apps import AppConfig


class SellerConfig(AppConfig):
    name = 'seller'

    def ready(sekf):
        import seller.signals