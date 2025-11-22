from django.contrib import admin
from skill.models import Skill

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name' , 'is_active' , 'created_at', 'updated_at']
    ordering = ['-updated_at']
    search_fields = ['name']
    list_editable = ['is_active']
    


admin.site.register(Skill , SkillAdmin)



