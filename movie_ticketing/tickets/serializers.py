from rest_framework import serializers
from .models import Movie, Screening, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
def get_image(self, obj):
    if obj.image:
        return obj.image.url
    return None

class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
