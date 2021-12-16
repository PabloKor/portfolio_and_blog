from django.db import models

# Create your models here.
from django.utils import timezone


class Bloging(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
