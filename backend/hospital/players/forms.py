from django import forms


class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        widgets = {
        'password': forms.PasswordInput(),
    }