from django.contrib import admin

from .models import UserDetails,UserMore,Prescription,CreatePatient,patientInvoice

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(UserMore)
admin.site.register(Prescription)
admin.site.register(CreatePatient)
admin.site.register(patientInvoice)

