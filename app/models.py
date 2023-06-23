from django.db import models

# Create your models here.

class Restaurant(models.Model):
    rest_id = models.TextField()
    name = models.CharField(max_length=2000)
    location = models.CharField(max_length=2000)
    items = models.TextField()
    lat_long = models.CharField(max_length=2000)
    full_details = models.TextField()
    rating = models.CharField(default='0', max_length=10)

    def __str__(self):
        return self.name