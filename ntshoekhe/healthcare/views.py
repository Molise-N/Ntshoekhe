from django.shortcuts import render
from .models import Hospital ,Patient ,Doctor

# Create your views here.

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})

def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    return render(request, 'hospital_detail.html', {'hospital': hospital})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient_detail.html', {'patient': patient})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})