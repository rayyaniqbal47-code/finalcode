from django.urls import path
from jobseeker import views

urlpatterns = [
    path('profile/' , views.profile , name='profile'),
    path('edit_jobseekerprofile/' , views.edit_jobseekerprofile , name='edit_jobseekerprofile'),

    path('profile/add_experience/' , views.add_experience , name='add_experience'),
    path('profile/edit_experience/<int:pk>/' , views.edit_experience , name='edit_experience'),
    path('profile/delete_experience/<int:pk>/' , views.delete_experience , name='delete_experience'),

    path('profile/add_education/' , views.add_education , name='add_education'),
    path('profile/edit_education/<int:pk>/' , views.edit_education , name='edit_education'),
    path('profile/delete_education/<int:pk>/' , views.delete_education , name='delete_education'),

    path('profile/add_skill/' , views.add_skill , name='add_skill'),
    path('profile/delete_skill/<int:pk>/' , views.delete_skill , name='delete_skill'),
]




