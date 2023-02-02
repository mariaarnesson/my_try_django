from django.urls import path 
from . import views
from .views import AddReservationView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', AddReservationView.as_view(), name='add'),
]