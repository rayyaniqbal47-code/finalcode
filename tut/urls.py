from django.urls import path
from tut import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('job_detail/<slug:job_slug>/' , views.job_detail , name='job_detail'),
]

