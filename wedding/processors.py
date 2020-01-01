from django.conf import settings

def bride_and_groom_processor(request):
    return {
        'bride_and_groom': settings.BRIDE_AND_GROOM,
    }
