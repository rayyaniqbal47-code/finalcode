from django.urls import path
from adminsetup import views

urlpatterns = [
    path('add_job/' , views.add_job , name='add_job'),
    path('edit_job/<slug:job_slug>/' , views.edit_job , name='edit_job'),
    path('delete_job/<int:pk>/' , views.delete_job , name='delete_job'),
    path('all_jobs_admin_dashboard/' , views.all_jobs_admin_dashboard , name='all_jobs_admin_dashboard'),

    path('applications/' , views.applications , name='applications'),
    path('application/<int:pk>/accept/', views.accept_application, name='accept_application'),
    path('application/<int:pk>/reject/', views.reject_application, name='reject_application'),

    path('jobseeker_users/' , views.jobseeker_users , name='jobseeker_users'),
    path('application/<int:pk>/suspend_user/', views.suspend_user, name='suspend_user'),
    path('application/<int:pk>/unsuspend_user/', views.unsuspend_user, name='unsuspend_user'),

    path('admin_audit_dashboard/' , views.admin_audit_dashboard , name='admin_audit_dashboard'),
]

