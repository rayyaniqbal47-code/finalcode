from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required , user_passes_test
from adminsetup.models import Job
from adminsetup.forms import AddJobForm
from accounts.views import check_admin_perms
from django.template.defaultfilters import slugify
from django.utils import timezone 
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from applications.models import Application
from accounts.models import CustomUser


# Create your views here.

@login_required
@user_passes_test(check_admin_perms)
def add_job(request):

    if request.method == 'POST':

        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            form.save_m2m()
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            job.job_slug = f"{slugify(job.title)}-{job.pk}-{timestamp}"
            job.save()
            return redirect('admin_dashboard')   
        else:
            print(form.errors)         

    else:
        form = AddJobForm()
    context = {
        'form':form,
    }
    return render(request, 'adminsetup/add_job.html' , context)


@login_required
@user_passes_test(check_admin_perms)
def edit_job(request , job_slug):
    job = get_object_or_404(Job , job_slug=job_slug)
    old_title = job.title

    if request.method == 'POST':
        
        form = AddJobForm(request.POST , instance=job)

        if form.is_valid():
            job = form.save(commit=False)

            if job.title != old_title:
                timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
                job.job_slug = f"{slugify(job.title)}-{job.pk}-{timestamp}"
            
            job.save()
            form.save_m2m()

            return redirect('all_jobs_admin_dashboard')
        
    else:
        form = AddJobForm(instance=job)

    context = {
        'form':form,
        'job': job,
    }

    return render(request, 'adminsetup/edit_job.html'  , context)


@login_required
@user_passes_test(check_admin_perms)
def delete_job(request , pk):
    job = get_object_or_404(Job , pk=pk)
    job.delete()
    
    return redirect('all_jobs_admin_dashboard')


@login_required
@user_passes_test(check_admin_perms)
def all_jobs_admin_dashboard(request):
    jobs = Job.objects.filter(is_active=True)
    paginator = Paginator(jobs , 2)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)
    context = {
        'jobs':paged_jobs,
    }
    return render(request, 'adminsetup/all_jobs_admin_dashboard.html' , context)    


@login_required
@user_passes_test(check_admin_perms)
def applications(request):
    applications = Application.objects.select_related('job', 'jobseeker').order_by('-applied_at')

    paginator = Paginator(applications, 1)  
    page_number = request.GET.get('page')
    applications_page = paginator.get_page(page_number)

    context = {
        'applications':applications_page,
    }
    return render(request, 'adminsetup/applications.html' , context)


@login_required
@user_passes_test(check_admin_perms)
def accept_application(request, pk):
    application = get_object_or_404(Application, id=pk)
    application.status = "accepted"
    application.save()
    return redirect('applications')


@login_required
@user_passes_test(check_admin_perms)
def reject_application(request, pk):
    application = get_object_or_404(Application, id=pk)
    application.status = "rejected"
    application.save()
    return redirect('applications')


@login_required
@user_passes_test(check_admin_perms)
def jobseeker_users(request):
    users = CustomUser.objects.filter(is_job_seeker=True)
    context = {
        'users':users,
    }
    return render(request, 'adminsetup/jobseeker_users.html' , context)


@login_required
@user_passes_test(check_admin_perms)
def suspend_user(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=pk)
        user.is_active = False
        user.is_suspended = True  
        user.save()
    return redirect('jobseeker_users')


@login_required
@user_passes_test(check_admin_perms)
def unsuspend_user(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=pk)
        user.is_active = True  
        user.is_suspended = False
        user.save()
    return redirect('jobseeker_users')



