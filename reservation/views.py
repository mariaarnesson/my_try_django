
from . forms import AddForm
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic.edit import CreateView


class AddReservationp(CreateView):

    form_class = ReservationForm
    template_name = 'reservation_create_form.html'
    success_url = '/reservation/'
