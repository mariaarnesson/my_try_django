from django import forms
from reservation.models import User, Reservation
from django.conf import settings


class ReservationForm(forms.ModelForm):
    date_reserved = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': 'yyyy-mm-dd',
               'id': 'datepicker'}), required=True,)
    resto_type=forms.RadioSelect()

    class Meta:
        model = Reservation
        fields = ['first_name', 'resto_type',
                  'email', 'people', 'time',
                  'date_reserved', 'status']


class ReservationUpdateForm(forms.ModelForm):
    time = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'timepicker',
                                      'class': 'input-group'}))
    date_reserved = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': 'yyyy-mm-dd',
               'id': 'datepicker'}), required=True,)
    resto_type=forms.RadioSelect()

    class Meta:
        model = Reservation
        fields = ['first_name',
                  'email', 'people', 'time',
                  'date_reserved', 'status']

