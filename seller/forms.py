from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserupdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username",)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields= ['image']