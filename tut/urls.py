from django.urls import path
from tut import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('job_detail/<slug:job_slug>/' , views.job_detail , name='job_detail'),
    path('jobs_list/' , views.jobs_list , name='jobs_list'),
    path('recommended_jobs_view/' , views.recommended_jobs_view , name='recommended_jobs_view'),
    path('job_search/' , views.job_search , name='job_search'),
]

