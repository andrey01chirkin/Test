from datetime import datetime
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from appointment_app.models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'appointment_app/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()
        # html_content = render_to_string(
        #     'appointment_created.html',
        #     {
        #         'appointment': appointment,
        #     }
        # )
        return redirect('appointment_view')