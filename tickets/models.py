from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
# Guest , Movie , Reservation


class Movie(models.Model):
    Hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    # date = models.DateField(max_length=10)

    def __str__(self):
        return self.movie



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()


    def __str__(self):
        return self.title






class Guest(models.Model):
    name = models.CharField(max_length=20)
    phone  = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='guest_reservation')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reservation')

    def __str__(self):
        return f"{self.guest} has booked {self.movie}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)