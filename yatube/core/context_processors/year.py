from django.utils import timezone


def year(request):
    """Add year varable."""
    return {
        'year': timezone.now().year,
    }
