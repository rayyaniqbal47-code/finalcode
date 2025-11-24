from django.shortcuts import render , redirect , get_object_or_404
from adminsetup.models import Job
from applications.models import Application
from jobseeker.models import JobBookmark

# Create your views here.

def home(request):
    jobs = Job.objects.filter(is_active=True)
    context = {
        'jobs':jobs,
    }
    return render(request , 'tut/home.html' , context)


def job_detail(request, job_slug):
    job = get_object_or_404(Job, is_active=True, job_slug=job_slug)

    application = None
    if request.user.is_authenticated and hasattr(request.user, 'customuserprofile'):
        jobseeker = request.user.customuserprofile
        application = Application.objects.filter(job=job, jobseeker=jobseeker).first()

    is_bookmarked = False
    if request.user.is_authenticated:
        is_bookmarked = JobBookmark.objects.filter(
            user=request.user, 
            job=job
        ).exists()
    

    context = {
        'job': job,
        'application': application,
        'is_bookmarked': is_bookmarked,
    }
    return render(request, 'tut/job_detail.html', context)




