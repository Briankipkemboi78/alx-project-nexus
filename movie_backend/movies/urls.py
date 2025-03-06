from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, TrendingMoviesView, RecommendedMoviesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('movies/trending/', TrendingMoviesView.as_view(), name='trending_movies'),
    path('movies/recommended/', RecommendedMoviesView.as_view(), name='recommended_movies'),
]
