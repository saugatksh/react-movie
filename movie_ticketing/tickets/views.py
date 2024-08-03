from rest_framework import viewsets
from .models import Movie, Screening, Booking
from .serializers import MovieSerializer, ScreeningSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
