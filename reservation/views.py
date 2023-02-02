from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from django.views.generic.edit import CreateView
from . forms import AddForm
# def home(request):
#    return render(request, "home.html", {})


class AddReservationView(CreateView):
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/reservation/'
