from django.db import models
from django.urls import reverse

SERVICES = (
   ('R', 'Restringing'),
   ('I', 'Intonation'),
   ('D', 'Detailing')
)

# Create your models here.
class Guitar(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strings = models.IntegerField()

def __str__(self):
        return f'{self.name} ({self.id})'      
# **************************************

def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})

def maintain_for_today(self):
     return self.maintenance_set.filter(date=date.today()).count() >= len(SERVICES)

class Maintenance(models.Model):
  date = models.DateField()
  service = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[0][0])

guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_service_display()} on {self.date}"

    