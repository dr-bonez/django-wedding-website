from urllib.parse import urlparse

from django.conf import settings
from django.shortcuts import redirect, render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    main_host = urlparse(settings.WEDDING_WEBSITE_URL).hostname
    request_host = request.get_host().split(':')[0]
    if main_host and request_host != main_host:
        return redirect(settings.WEDDING_WEBSITE_URL, permanent=False)
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'website_url': settings.WEDDING_WEBSITE_URL,
        'couple_name': settings.BRIDE_AND_GROOM,
        'wedding_location': settings.WEDDING_LOCATION,
        'wedding_date': settings.WEDDING_DATE,
    })
