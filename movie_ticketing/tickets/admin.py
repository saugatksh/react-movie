from django.contrib import admin
from .models import Movie, Screening, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'description', 'image','trailer_url')
    search_fields = ('title',)
    list_filter = ('release_date',)
    ordering = ('-release_date',)
    fields = ('title', 'description', 'release_date','image','trailer_url')
    # readonly_fields = ('description',)

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('movie', 'screening_time', 'available_seats')
    search_fields = ('movie__title',)
    list_filter = ('screening_time', 'movie')
    ordering = ('-screening_time',)
    fields = ('movie', 'screening_time', 'available_seats')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'screening', 'seats',)
    search_fields = ('user_name', 'screening__movie__title')
    list_filter = ('screening__screening_time', 'seats')
    ordering = ('-screening__screening_time',)
    fields = ('user_name', 'screening', 'seats')
