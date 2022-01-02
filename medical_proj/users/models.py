from django.db import models

# Create your models here.

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(default='')
    patient_type = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=255)
    covid_positive = models.CharField(max_length=10)
    date_time = models.DateTimeField(default=None)
    patient_description = models.TextField(default="")