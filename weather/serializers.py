from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=100)
