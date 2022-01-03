from django.contrib import admin
from .models import Appointment, OxygenAvailability


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name','age','sex', 'doctor_name', 'date_time', 'patient_type')  # fields to display in the listing
    list_filter = ('doctor_name', 'sex')      # enable results filtering
    list_per_page = 25                     # number of items per page 
    ordering = ['-date_time', 'patient_name']       # Default results ordering



class OxygenAvailabilityAdmin(admin.ModelAdmin):
    # form = OxygenForm
    list_display = ('oxygen_type', 'amount', 'address')
    list_per_page = 25
    fields = ('oxygen_type', 'amount',)


# and register it 
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(OxygenAvailability, OxygenAvailabilityAdmin)