from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import LocationSerializer

class WeatherHomeView(TemplateView):
    template_name = 'weather/index.html'

class WeatherAPIView(generics.GenericAPIView):
    serializer_class = LocationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location = serializer.validated_data['location']

        try:
            response = requests.get(
                'http://api.openweathermap.org/data/2.5/weather',
                params={
                    'q': location,
                    'appid': settings.OPENWEATHER_API_KEY,
                    'units': 'metric'
                },
                timeout=5
            )
            response.raise_for_status()
            data = response.json()

            return Response({
                'location': location,
                'temp': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": "Weather service unavailable"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )