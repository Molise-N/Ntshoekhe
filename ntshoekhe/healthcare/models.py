from django.db import models
from django.utils.translation import gettext_lazy as _

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.hospital_name

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    condition = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name
