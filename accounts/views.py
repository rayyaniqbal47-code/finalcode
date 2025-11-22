from django.shortcuts import render , redirect , get_object_or_404
from accounts.forms import CustomUserForm
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib import auth
from accounts.utils import detectuser
from django.contrib.auth.decorators import login_required , user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.


# restrict the jobseeker from accessing the admin page

def check_jobseeker_perms(user):

    if user.is_staff or user.is_superadmin:
        raise PermissionDenied
    
    if user.is_job_seeker:
        return True
    else:
        return PermissionDenied


# restrict the admin from accessing the jobseeker page

def check_admin_perms(user):
    if user.is_staff and user.is_superadmin:
        return True
    else:
        raise PermissionDenied
    


def registration(request):

    if request.user.is_authenticated:
        return redirect('myAccount')

    elif request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():

            # create the user using create_user method

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.is_job_seeker = True
            user.save()
            messages.success(request , 'account register successfully')

            # send verification email

            mail_subject = 'please activate your account'

            email_template = 'accounts/emails/accounts_verification_email.html'

            #send_verification_email(request , user , mail_subject , email_template)

            return redirect('registration')

    else:
        form = CustomUserForm()
    context = {
        'form':form,
    }
    return render(request , 'accounts/registration.html' , context)



def login(request):

    if request.user.is_authenticated:
        return redirect('myAccount')

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email , password=password)
        if user is not None:

            auth.login(request , user)
            messages.success(request , 'login success')

            return redirect('myAccount')
        else:
            return redirect('login')
    return render(request , 'accounts/login.html')


@login_required
def logout(request):

    if request.method == 'POST':

        auth.logout(request)
        messages.success(request , 'logout success')

        return redirect('login')

@login_required
def myAccount(request):

    user = request.user
    redirecturl = detectuser(user=user)

    return redirect(redirecturl)


@login_required
@user_passes_test(check_admin_perms)
def admin_dashboard(request):
    return render(request , 'accounts/admin_dashboard.html')

@login_required
@user_passes_test(check_jobseeker_perms)
def jobseeker_dashboard(request):
    return render(request , 'accounts/jobseeker_dashboard.html')


