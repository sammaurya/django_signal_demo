from django.apps import AppConfig


class SignalDemoAppConfig(AppConfig):
    name = 'signal_demo_app'

    def ready(self):
        import signal_demo_app.signals
