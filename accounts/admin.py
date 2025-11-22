from django.contrib import admin
from accounts.models import CustomUser , CustomUserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display = ['email' , 'first_name' , 'last_name' , 'username' , 'is_active' , 'is_superadmin' , 'is_job_seeker']
    ordering = ['-date_joined']



admin.site.register(CustomUser , CustomUserAdmin)

class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ('customuser', 'total_years_of_experience', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'skills')  
    search_fields = ('customuser__username', 'bio')      

admin.site.register(CustomUserProfile, CustomUserProfileAdmin)






