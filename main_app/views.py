from django.shortcuts import render

guitars = [
    {'model': 'Telecaster', 'manufacturer': 'Fender', 'description': 'solid-body electric guitar', 'strings': 6},
    {'model': 'C5-CE', 'manufactuter': 'Cordoba', 'description': 'nylon-string electric classical guitar', 'strings': 6},
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', {
        'guitars': guitars
    })