from django.conf import settings

def settings_processor(request):
    return {
        'bride_and_groom': settings.BRIDE_AND_GROOM,
        'site_url': settings.WEDDING_WEBSITE_URL,
    }
