from django import forms
from .models import test_model

class test_form(forms.ModelForm):
    class Meta:
        model = test_model
        fields = ['name','email']