# views.py
import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Favorite
from django.conf import settings



def add_favorite(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = json.loads(request.body)
            place_id = data.get('place_id')
            name = data.get('name')
            if place_id:
                favorite, created = Favorite.objects.get_or_create(user=request.user, place_id=place_id, name=name)
                return JsonResponse({'success': created})  # Return success response
            else:
                return JsonResponse({'error': 'place_id is required'}, status=469)
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=403)



def user_favorites(request):
    saved_restaurants = Favorite.objects.filter(user=request.user).order_by(
        'place_id')  # Or another field if you have one
    # print(saved_restaurants)
    key = settings.GOOGLE_API_KEY
    context = {
        'key': key,
        'saved_restaurants': saved_restaurants
    }
    return render(request, 'favorites/favorites.html', context)