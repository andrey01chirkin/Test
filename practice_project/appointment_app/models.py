from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    date = models.DateField(default=timezone.now)
    client_name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'
