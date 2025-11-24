from django.contrib import admin
from applications.models import Application

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'jobseeker', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'job')
    search_fields = (
        'job__title', 
        'jobseeker__customuser__username', 
        'jobseeker__customuser__email'
    )
    ordering = ('-applied_at',)


admin.site.register(Application , ApplicationAdmin)


