from django import forms
from .models import upload

class createForm(forms.ModelForm):

    class Meta:
        model = upload
        fields = ['photo','comment']
   