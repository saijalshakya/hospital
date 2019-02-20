from django import forms

class DoctorForm(forms.Form):
    name = forms.CharField()