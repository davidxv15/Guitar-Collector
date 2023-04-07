import os
from django.shortcuts import render, redirect
# importing guitar MODEL
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Pedal
from .forms import MaintenanceForm

guitars = [
    {'model': 'Telecaster', 'manufacturer': 'Fender', 'description':'Solid-body electric guitar', 'strings': 6},
    {'model': 'C5-CE', 'manufacturer': 'Cordoba', 'description':'Nylon-string electric classical guitar', 'strings': 6},
    {'model': 'Banjo', 'manufacturer': 'Fender', 'description': '5-string banjo', 'strings': 5},
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {
        'guitars': guitars
    })

def guitars_detail(request, guitar_id):
  guitar = Guitar.objects.get(id=guitar_id)
  id_list = guitar.pedals.all().values_list('id')
  pedals_guitar_doesnt_have = Pedal.objects.exclude(id__in=id_list)
  maintenance_form = MaintenanceForm()
  return render(request, 'guitars/detail.html', {
     'guitar': guitar, 'maintenance_form': maintenance_form, 'pedals': pedals_guitar_doesnt_have
  })

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['model', 'manufacturer', 'description', 'strings']
    success_url = '/guitars/'
    # {guitar_id}

class GuitarUpdate(UpdateView):
  model = Guitar
  # Let's disallow the renaming of a guitar by excluding the name field!
  fields = ['model', 'manufacturer', 'description', 'strings']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars'

def add_maintenance(request, guitar_id):
   form = MaintenanceForm(request.POST)
   if form.is_valid():
      new_maintenance = form.save(commit=False)
      new_maintenance.guitar_id = guitar_id
      new_maintenance.save()
   return redirect('detail', guitar_id=guitar_id)

class PedalList(ListView):
  model = Pedal

class PedalDetail(DetailView):
  model = Pedal

class PedalCreate(CreateView):
  model = Pedal
  fields = '__all__'

class PedalUpdate(UpdateView):
  model = Pedal
  fields = ['name', 'color']

class PedalDelete(DeleteView):
  model = Pedal
  success_url = '/pedals'


def assoc_pedal(request, guitar_id, pedal_id):
  Guitar.objects.get(id=guitar_id).pedals.add(pedal_id)
  return redirect('detail', guitar_id=guitar_id)


def unassoc_pedal(request, guitar_id, pedal_id):
  Guitar.objects.get(id=guitar_id).pedals.remove(pedal_id)
  return redirect('detail', guitar_id=guitar_id)