from django.shortcuts import render
# importing guitar MODEL
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar
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
  maintenance_form = MaintenanceForm()
  return render(request, 'guitars/detail.html', { 'guitar': guitar, 'maintenance_form': maintenance_form })

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['model', 'manufacturer', 'description', 'strings']
    success_url = '/guitars/'
    # {guitar_id}

class GuitarUpdate(UpdateView):
  model = Guitar
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['model', 'manufacturer', 'description', 'strings']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars'