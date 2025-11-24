from django.urls import path
from adminsetup import views

urlpatterns = [
    path('add_job/' , views.add_job , name='add_job'),
    path('edit_job/<slug:job_slug>/' , views.edit_job , name='edit_job'),
    path('delete_job/<int:pk>/' , views.delete_job , name='delete_job'),
    path('all_jobs_admin_dashboard/' , views.all_jobs_admin_dashboard , name='all_jobs_admin_dashboard'),
]

