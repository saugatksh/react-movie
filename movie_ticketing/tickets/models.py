from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    trailer_url = models.URLField(max_length=200, blank=True, null=True)



    def __str__(self):
        return self.title

class Screening(models.Model):
    movie = models.ForeignKey(Movie, related_name='screenings', on_delete=models.CASCADE)
    screening_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.movie.title} at {self.screening_time}'

class Booking(models.Model):
    screening = models.ForeignKey(Screening, related_name='bookings', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return f'{self.user_name} booked {self.seats} seats for {self.screening.movie.title}'
