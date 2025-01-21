from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    name = 'appointment_app'

    def ready(self):
        import appointment_app.signals

