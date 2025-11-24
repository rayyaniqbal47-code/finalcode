from django.urls import path , include
from accounts import views

urlpatterns = [
    path('registration/' , views.registration , name='registration'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
    path('myAccount/' , views.myAccount , name='myAccount'),
    path('admin_dashboard/' , views.admin_dashboard , name='admin_dashboard'),
    path('jobseeker_dashboard/' , views.jobseeker_dashboard , name='jobseeker_dashboard'),

    path('activate/<uidb64>/<token>/' , views.activate , name='activate'),


    path('forgot_password/' , views.forgot_password , name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/' , views.reset_password_validate , name='reset_password_validate'),
    path('reset_password/' , views.reset_password , name='reset_password'),


    path('password_change/' , views.password_change , name='password_change'),


    
    path('admin_dashboard/' , include('adminsetup.urls')),

    path('jobseeker_dashboard/' , include('jobseeker.urls')),

    

]



