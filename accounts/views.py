from django.shortcuts import render , redirect
from accounts.forms import CustomUserForm
from accounts.models import CustomUser
from django.contrib import messages

# Create your views here.

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

