from django.urls import path
from . import views
from search.views import search_nearby_restaurants

urlpatterns = [
    path('', views.sign_in, name="map"),
]