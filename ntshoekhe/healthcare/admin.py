from django.contrib import admin
from .models import Hospital, Patient , Doctor

admin.site.site_header = "ntshoekhoe"
admin.site.site_title = "ntshoekhoe admin area"
admin.site.site_index_title= "welcome to ntshoekhoe admin area"

admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Doctor)

