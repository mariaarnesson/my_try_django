from django import forms
from .models import Reservation


class AddForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'date', 'time', 'no_of_guest', 'table', 'no_of_guest')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
           # 'date': forms.DateInput(attrs={'class': 'form-control'}),
           # 'time': forms.TimeInput(attrs={'class': 'form-control'}),
           # 'no_of_guest': forms.NumberInput(attrs={'class': 'form-control'}),
           # 'table': forms.TABLE_CHOICESInput(attrs={'class': 'form-control'})
        }
