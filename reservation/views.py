from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReservationForm
from .models import Reservation
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


class AddReservationView(SuccessMessageMixin, CreateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create_form.html'
    success_url = '/reservation/'
    success_message = 'Reservation created!'

    # Set reservation user to current logged in user and ensure form is valid
    # before save
    def form_valid(self, form):
        form.instance.user = self.request.user
        user = User.objects.get(username=self.request.user.username)
        userReservations = Reservation.objects.filter(user=user)
        error = False
        # loop through the reservations
        for reservation in userReservations:
            # check if any are the same as the date in the form
            if str(reservation.date) == self.request.POST["date"]:
                error = True

        if error is True:
            form.add_error(
                'date',
                'You have booked this day already. Try another date.'
                )
            return super(AddReservationView, self).form_invalid(form)
        else:
            self.object = form.save()
            return super().form_valid(form)

    # Display a list of all reservations

    
class ReservationListView(ListView):

    model = Reservation
    template_name = 'reservation_list.html'

    # Get object data and return it
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['current'] = Reservation.objects.all()
        else:
            context['current'] = Reservation.objects.filter(
                user=self.request.user
                )
        return context


# Update selected reservation
class ReservationUpdateView(SuccessMessageMixin, UpdateView):

    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_update_form.html'
    success_url = '/reservation/list/'
    success_message = 'Reservation updated!'


# Delete selected reservation
class ReservationDeleteView(SuccessMessageMixin, DeleteView):

    model = Reservation
    success_url = reverse_lazy('reservation_list')
