from django.urls import path
from adminsetup import views

urlpatterns = [
    path('add_job/' , views.add_job , name='add_job'),
]

