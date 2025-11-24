from django.contrib import admin
from .models import Experience , Education , JobBookmark

# Register your models here.


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'company_name', 'role', 'years')
    list_filter = ('profile', 'company_name', 'role')
    search_fields = ('company_name', 'role', 'profile__customuser__email')
    ordering = ('profile', 'company_name')


admin.site.register(Experience , ExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'institution_name', 'degree', 'start_year', 'end_year')
    
    search_fields = ('institution_name', 'degree', 'profile__user__username')
    
    list_filter = ('degree', 'start_year', 'end_year')
    
    ordering = ('-start_year',)

admin.site.register(Education , EducationAdmin)


class JobBookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__email', 'job__title')
    ordering = ('-created_at',)


admin.site.register(JobBookmark , JobBookmarkAdmin)


