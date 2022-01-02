import traceback 
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from .models import Appointment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def appointment(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name", "")
            sex = request.POST.get("sex", "")
            age = request.POST.get("age", "")
            email = request.POST.get("email", "")
            doctor = request.POST.get("doctor", "")
            patient_type = request.POST.get("type", "")
            covid = request.POST.get("covid", "")
            the_date = request.POST.get("day", "")
            the_hour = request.POST.get("hour", "")
            the_min = request.POST.get("min", "")
            am_pm = request.POST.get("am_pm", "")

            description = request.POST.get("description", "")
            date_time = datetime.strptime(the_date+' '+the_hour+':'+the_min+' '+am_pm, '%Y-%m-%d %I:%M %p')

            Appointment(patient_name=name, sex=sex, age=age, email=email, doctor_name=doctor, patient_type=patient_type,
                covid_positive=covid, date_time=date_time, patient_description=description).save()
            
            return JsonResponse({"message": 1})
            
        except Exception as e:
            print(traceback.format_exc())
    return JsonResponse({"message": 100})