from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class updateduserform(forms.ModelForm):
    class Meta:
            model = UserCreationForm
            fields = [ ' username ', 'email', 'password', ]
            