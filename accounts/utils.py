from accounts.models import CustomUser , CustomUserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings

def detectuser(user):
    if user.is_staff and user.is_superadmin:
        redirecturl = 'admin_dashboard'
        return redirecturl
    elif user.is_job_seeker:
        redirecturl = 'jobseeker_dashboard'
        return redirecturl
    


