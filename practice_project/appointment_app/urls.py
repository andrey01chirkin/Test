from django.urls import path
from .views import AppointmentView

urlpatterns = [
    path('send_email/', AppointmentView.as_view(), name='appointment_view'),
]