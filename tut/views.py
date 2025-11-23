from django.shortcuts import render
from adminsetup.models import Job

# Create your views here.

def home(request):
    jobs = Job.objects.filter(is_active=True)
    context = {
        'jobs':jobs,
    }
    return render(request , 'tut/home.html' , context)


