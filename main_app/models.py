from django.db import models
from django.urls import reverse
from datetime import date

SERVICES = (
   ('R', 'Restringing'),
   ('I', 'Intonation'),
   ('D', 'Detailing')
)

# Create your models here.
class Pedal(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pedals_detail', kwargs={'pk': self.id})


class Guitar(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    strings = models.IntegerField()
    pedals = models.ManyToManyField(Pedal)

    def __str__(self):
        return f'{self.model} ({self.id})'    
   
    def get_absolute_url(self):
        return reverse('detail', kwargs= {'guitar_id': self.id})

    def maintain_for_today(self):
     return self.maintenance_set.filter(date=date.today()).count() >= len(SERVICES)

class Maintenance(models.Model):
  date = models.DateField('Maintenance Date')
  service = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[0][0])

  guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, default=1)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_service_display()} on {self.date}"
  
  class Meta:
     ordering = ['-date']

    