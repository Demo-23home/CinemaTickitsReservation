from django.db import models


# Guest , Movie , Reservation


class Movie(models.Model):
    Hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField(max_length=10)

    def __str__(self):
        return self.movie




class Guest(models.Model):
    name = models.CharField(max_length=20)
    phone  = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='guest_reservation')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reservation')

