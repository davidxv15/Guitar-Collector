from django.db import models
from django.urls import reverse

# Create your models here.
class Guitar(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strings = models.IntegerField()

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})