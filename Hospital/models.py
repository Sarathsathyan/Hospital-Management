from django.db import models

from django.contrib.auth.models import User
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UserDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    user_phone = PhoneNumberField(null=False, blank=False, unique=False, default='+91')
    user_pass = models.CharField(max_length=10, blank=True)
    user_role = models.CharField(max_length=100,null=True)
    user_date = models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return str(self.user_id) if self.user_id else ''

class UserMore(models.Model):
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    case = models.IntegerField()
    blood = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.gender

class Prescription(models.Model):
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    prescrip = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return self.patient

class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=100)
    patient =  models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.date

class CreatePatient(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=False, default='+91')
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100,null=True)
    out = models.CharField(max_length=100,null=True)
    paid = models.CharField(max_length=50,null=True)
    case = models.CharField(max_length=100,null=True)
    group = models.CharField(max_length=50,null=True)

    create_date = models.DateTimeField(default=datetime.now,null=True)

    def __str__(self):
        return self.name


class patientInvoice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    paid = models.IntegerField()
    date = models.DateTimeField(default=datetime.now,null=True)
    outstand = models.IntegerField()


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=False, default='+91')
    date = models.DateField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.name



