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