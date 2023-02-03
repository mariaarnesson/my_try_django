from django.forms import ModelForm
from django import forms
from .models import Reservation
import datetime
from django.core.exceptions import ValidationError


class ReservationForm(ModelForm):

    # compare user input with current date and raise error if in past or
    # current
    def clean_date(self):
        date = self.cleaned_data['date']
        if date <= datetime.date.today():
            raise ValidationError(
                message='Date cannot be in the past or today'
                )
        return date

    class Meta:
        model = Reservation
        fields = ['name', 'seats', 'date', 'time']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',
                    }
            ),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a time',
                    'type': 'time',
                    }

            ),
        }


class EditReservations(forms.ModelForm):
    # compare user input with current date and raise error if in past or
    # current
    def clean_date(self):
        date = self.cleaned_data['date']
        if date <= datetime.date.today():
            raise ValidationError(message='Date cannot be in the past')
        return date

    class Meta:
        model = Reservation
        fields = ['name', 'seats', 'date', 'time']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    }
            ),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={
                    'class': 'form-control',
                    'type': 'time',
                    }

            ),
        }