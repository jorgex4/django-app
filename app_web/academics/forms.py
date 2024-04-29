from django import forms
from academics.models import User

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'status'
        ]