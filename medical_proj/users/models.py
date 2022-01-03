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



OXYGEN_TYPE_CHOICES=(
    ('CGS', 'Compressed Gas System'),
    ('POC', 'Portable Oxygen Concentrators'),
    ('LOS', 'Liquid Oxygen Systems'),
)


class OxygenAvailability(models.Model):
    oxygen_type = models.CharField(choices=OXYGEN_TYPE_CHOICES, max_length=4, default='CGS')
    amount = models.PositiveSmallIntegerField(default=0)
    address = models.TextField(default="")