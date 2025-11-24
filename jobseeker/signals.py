from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from jobseeker.models import Experience
from django.db.models import Sum

@receiver(post_save, sender=Experience)
def update_or_save_total_experience(sender, instance, **kwargs):
    profile = instance.profile
    total_years = profile.experience_set.aggregate(total=Sum('years'))['total'] or 0
    profile.total_years_of_experience = total_years
    profile.save()    


@receiver(post_delete, sender=Experience)
def update_total_years_on_delete(sender, instance, **kwargs):
    profile = instance.profile
    total_years = profile.experience_set.aggregate(total=Sum('years'))['total'] or 0
    profile.total_years_of_experience = total_years
    profile.save()
