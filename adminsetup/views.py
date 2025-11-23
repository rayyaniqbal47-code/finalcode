from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required , user_passes_test
from adminsetup.models import Job
from adminsetup.forms import AddJobForm
from accounts.views import check_admin_perms
from django.template.defaultfilters import slugify
from django.utils import timezone 

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



