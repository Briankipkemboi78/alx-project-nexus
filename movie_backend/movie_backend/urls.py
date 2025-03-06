
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

def home_view(request):
    return JsonResponse({"message": "Welcome to the Movie Recommendation API!"})

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),
    
]
