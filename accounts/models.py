from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from skill.models import Skill
from .validators import validate_resume_extension

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self , first_name , last_name , username , email , password=None):

        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')
        
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name , 
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self , first_name , last_name , username , email , password=None):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name , 
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_job_seeker = False
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser):  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100 , unique=True)
    email = models.EmailField(max_length=100 , unique=True)
    phone_number = models.CharField(max_length=50 , blank=True)

    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)

    # for suspend
    is_suspended = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'first_name' , 'last_name']

    objects = CustomUserManager()
    

    def __str__(self):
        return self.email
    


    def has_perm(self , perm , obj=None):
        return self.is_admin
    

    def has_module_perms(self , app_label):
        return True
    
    


class CustomUserProfile(models.Model):
    customuser = models.OneToOneField(CustomUser , on_delete=models.CASCADE , blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    total_years_of_experience = models.FloatField(default=0)
    skills = models.ManyToManyField(Skill , blank=True)
    resume = models.FileField(upload_to='users/resumes' , blank=True, null=True, validators=[validate_resume_extension] , help_text="Upload your resume (PDF, DOCX)")
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  self.customuser.email if self.customuser else "No User"
    
    @property
    def resume_filename(self):
        if self.resume:
            return self.resume.name.split('/')[-1]
        return ''
    
    


    