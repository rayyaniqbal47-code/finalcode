from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def social_time(dt):
    now = timezone.now()
    diff = now - dt

    seconds = diff.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = diff.days

    if seconds < 60:
        return "Just now"
    elif minutes < 60:
        return f"{int(minutes)} minutes ago"
    elif hours < 24:
        return f"{int(hours)} hours ago"
    elif days < 7:
        return f"{int(days)} days ago"
    else:
        return dt.strftime("%b %d")  # Example: Nov 14




