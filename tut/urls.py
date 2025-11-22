from django.urls import path
from tut import views

urlpatterns = [
    path('' , views.home , name='home'),
]

