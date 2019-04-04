from django.db import models
from django.contrib.auth.models import User


class Train(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    speed = models.DecimalField(max_digits=6, decimal_places=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
