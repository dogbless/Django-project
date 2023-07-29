from django.db import models

class post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.CharField(max_length = 140)
    singnature = models.CharField(max_length = 140, default="Jesse")
    date = models.CharField(max_length = 140)

    def __str__(self):
        return self.title

# Create your models here.
