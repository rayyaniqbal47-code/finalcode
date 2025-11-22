from django.urls import path
from accounts import views

urlpatterns = [
    path('registration/' , views.registration , name='registration'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
    path('myAccount/' , views.myAccount , name='myAccount'),
    path('admin_dashboard/' , views.admin_dashboard , name='admin_dashboard'),
    path('jobseeker_dashboard/' , views.jobseeker_dashboard , name='jobseeker_dashboard'),
]



