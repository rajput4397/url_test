

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import URL
import json
from django.utils import timezone
import datetime
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Home page view
def home(request):
    return render(request, 'shortener/home.html')

# Shorten URL page view
def shorten_url(request):
    return render(request, 'shortener/shorten.html')

# Visit URL page view
def visit_url(request):
    return render(request, 'shortener/visit.html')

# Enquire page view
def enquire(request):
    return render(request, 'shortener/enquire.html')





@csrf_exempt  # Disable CSRF for simplicity
def check_url(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            original_url = data.get('url')  # Get the URL from the request

            if not original_url:
                return JsonResponse({"error": "URL is required"}, status=400)

            # Check if the URL already exists in the database
            url_entry = URL.objects.filter(url=original_url).first()

            if url_entry:
                # URL already exists
                return JsonResponse({"message": "URL already in use", "tiny_url": url_entry.tiny_url})

            # URL does not exist, so generate a new tiny URL
            # Generate unique tiny URL
            tiny_url = URL().generate_tiny_url()

            # Ensure the tiny URL is unique
            while URL.objects.filter(tiny_url=tiny_url).exists():
                tiny_url = URL().generate_tiny_url()  # Regenerate until unique

            # Create the new URL entry in the database
            expiration_days = data.get('expiration_time', 1)  # Default to 1 day if not provided
            expiration_time = timezone.now() + timezone.timedelta(days=int(expiration_days))

            # When creating the new URL entry, pass the expiration_time
            new_url_entry = URL(url=original_url, tiny_url=tiny_url, expiration_time=expiration_time)

            # new_url_entry = URL(url=original_url, tiny_url=tiny_url)
            new_url_entry.save()

            # Return the response with the new tiny URL
            return JsonResponse({"message": "URL is available", "tiny_url": tiny_url}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Return error for non-POST requests
    return JsonResponse({"error": "Invalid request method"}, status=405)

#for the rediredction
def redirect_to_original(request, tiny_url):
    try:
        url_entry = URL.objects.get(tiny_url=tiny_url)

        if timezone.now() > url_entry.expiration_time:
            url_entry.delete()  # Delete expired URL entry
            return JsonResponse({'error': 'URL has expired and no longer exists'}, status=404)

        # Increment access count
        url_entry.access_count += 1
        url_entry.save()

        # Return the original URL and any additional data you want
        return redirect(url_entry.url)

    except URL.DoesNotExist:
        return JsonResponse({'error': 'URL does not exist'}, status=404)
    

def enquire_url(request, tiny_url):
    try:
        url_entry=URL.objects.get(tiny_url=tiny_url)
        if timezone.now() > url_entry.expiration_time:
            # Delete the expired URL entry
            url_entry.delete()
            # Return a response indicating the URL does not exist
            return JsonResponse({'error': 'URL has expired and no longer exists'}, status=404)
        time_left=url_entry.expiration_time-timezone.now()

        return JsonResponse({
            'original_url': url_entry.url,
            'access_count': url_entry.access_count,
            'time_left_to_expire': str(time_left)  # Format the timedelta as a string
        })

    except URL.DoesNotExist:
        return JsonResponse({'error': 'URL does not exist'}, status=404)

