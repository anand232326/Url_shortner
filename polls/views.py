import redis
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import URLMapping
from .utils import encode_base62

redis_client = redis.Redis(
    host=settings.REDIS_HOST, 
    port=settings.REDIS_PORT, 
    decode_responses=True
)

def home_view(request):
    short_url = None
    error = None

    if request.method == "POST":
        long_url = request.POST.get("long_url")
        if long_url:
            try:
                url_obj = URLMapping.objects.create(long_url=long_url, short_key="temp")
                short_key = encode_base62(url_obj.id)
                url_obj.short_key = short_key
                url_obj.save(update_fields=["short_key"])
                
                redis_client.set(f"url:{short_key}", long_url, ex=86400)
                short_url = f"http://localhost/{short_key}"
            except Exception as e:
                error = f"An error occurred: {str(e)}"
        else:
            error = "Please provide a valid URL."

    return render(request, "polls/index.html", {
        "short_url": short_url,
        "error": error
    })

def redirect_view(request, short_key):
    cache_key = f"url:{short_key}"
    
    cached_long_url = redis_client.get(cache_key)
    if cached_long_url:
        return HttpResponseRedirect(cached_long_url)
        
    url_obj = get_object_or_404(URLMapping, short_key=short_key)
    redis_client.set(cache_key, url_obj.long_url, ex=86400)
    
    return HttpResponseRedirect(url_obj.long_url)