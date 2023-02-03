from django import forms
from .models import Reservation


class AddForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'date', 'no_of_guest', 'table')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
