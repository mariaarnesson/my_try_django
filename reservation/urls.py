from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booktable', views.booktable, name='booktable'),
    path('booktime', views.booktime, name='booktime'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('editbooking/<int:id>', views.editbooking, name='editbooking'),
    path('mybookings', views.mybooknings, name='mybookings'),
]