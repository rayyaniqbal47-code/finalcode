from accounts.models import CustomUser , CustomUserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save , sender=CustomUser)
def post_save_create_profile_recevier(sender , instance , created , **kwargs):
    
    if created:
        CustomUserProfile.objects.create(customuser=instance)
    else:
        try:
            profile = CustomUserProfile.objects.get(customuser=instance)
            profile.save()
        except:
            # create the user profile if not exist
            profile = CustomUserProfile.objects.create(customuser=instance)


            