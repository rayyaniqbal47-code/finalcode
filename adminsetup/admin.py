from django.contrib import admin
from adminsetup.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'state', 'city', 'job_type', 'experience_level', 'salary_min', 'salary_max', 'is_active', 'posted_at')
    list_filter = ('job_type', 'experience_level', 'state', 'is_active')
    search_fields = ('title', 'company_name', 'description', 'city', 'state')
    ordering = ('-posted_at',) 

admin.site.register(Job, JobAdmin)


