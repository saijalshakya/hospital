from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from doctor.models import Doctor

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password','is_staff','is_superuser']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldnames in ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']:
            self.fields[fieldnames].help_text = None
            self.fields[fieldnames].widget.attrs.update({'class': 'form-control autofocus'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2','is_staff','is_superuser')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'image', 'age', 'phone1', 'phone2', 'address', 'statement','status','educationStatement','service','type')
