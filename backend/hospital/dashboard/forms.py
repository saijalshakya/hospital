from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from doctor.models import Doctor, Service

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email', 'password','is_staff','is_superuser']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    is_staff = True
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

        toppings = forms.ModelMultipleChoiceField(queryset=Service.objects.all())
        def __init__(self, *args, **kwargs):
            # Only in case we build the form from an instance
            # (otherwise, 'toppings' list should be empty)
            if kwargs.get('instance'):
                # We get the 'initial' keyword argument or initialize it
                # as a dict if it didn't exist.                
                initial = kwargs.setdefault('initial', {})
                # The widget for a ModelMultipleChoiceField expects
                # a list of primary key for the selected data.
                initial['toppings'] = [t.pk for t in kwargs['instance'].topping_set.all()]

            forms.ModelForm.__init__(self, *args, **kwargs)