from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from weather.views import WeatherAPIView, WeatherHomeView

schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='v1',
        description="Get weather data with emoji-based advice!",
    ),
    public=True,
)

urlpatterns = [
    path('', WeatherHomeView.as_view(), name='weather-home'),
    path('api/weather/', WeatherAPIView.as_view(), name='weather-api'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]