from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('about/', views.About, name='about'),
    path('register/',views.Register,name='register'),
    path('Logout/',views.logout,name='logout'),
    path('doctor/',views.DoctorDashboard,name='doctorDash'),
    path('doctorProfile/',views.DoctorProfie,name='doctorProfile'),
    path('doctorAppoint/', views.DoctorAppointmnets, name='doctorAppointments'),
    path('doctorPrescription/', views.DoctorPrescription, name='doctorPrescription'),

    path('patientMedical/', views.PatientMedical, name='patientMedical'),

    path('reception/', views.ReceptionDash, name='receptionDash'),
    path('createAppointment/', views.ReceptionAppointment, name='receptionAppointment'),
    path('login/',views.UserLogin,name='login'),
    ]