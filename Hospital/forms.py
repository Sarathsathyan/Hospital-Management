from django.forms import ModelForm

from .models import UserDetails,User
from django.contrib.auth import authenticate


class AddUserForm(ModelForm):
    class Meta:
        model = UserDetails
        fields=['user_phone']