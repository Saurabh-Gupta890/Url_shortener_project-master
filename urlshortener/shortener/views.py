from django.shortcuts import render
from django.http import JsonResponse
from .models import ShortenedURL
from .utils import generate_short_code

def shorten_url(request):
    long_url = request.GET.get('url')
    if long_url:
        short_code = generate_short_code(long_url)
        while ShortenedURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code(long_url)
        obj, created = ShortenedURL.objects.get_or_create(long_url=long_url, defaults={'short_code': short_code})
        short_url = request.build_absolute_uri('/') + obj.short_code
        return JsonResponse({'short_url': short_url})
    return JsonResponse({'error': 'No URL provided'}, status=400)

def show_shorten_url_form(request):
    return render(request, 'shortener/shorten_url.html')