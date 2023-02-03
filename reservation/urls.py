from django.urls import path, include
from . import views
from .views import AddReservationView

urlpatterns = [
    path('', AddReservationCreate.as_view(), name='add'),
]
