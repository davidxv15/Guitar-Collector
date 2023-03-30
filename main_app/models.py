from django.db import models

# Create your models here.
class Guitar(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    strings = models.IntegerField()

    def __str__(self):
        return self.model