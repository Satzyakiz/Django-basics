from django import forms
from django.core import validators
from AppTwo.models import User


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = "__all__"
