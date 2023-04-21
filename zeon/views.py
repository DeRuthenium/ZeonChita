from django.shortcuts import render

# Create your views here.
from zeon.models import Tarifs, Computers


def render_index(request):
    computers = Computers.objects.all()
    context = {
        'computers': computers
    }
    return render(request, 'index.html')

def render_contacts(request):
    return render(request, 'contacts.html')

def render_catalog(request):
    tarifs=Tarifs.objects.all()
    context={
        'tarifs':tarifs
    }
    return render(request, 'catalog.html')

def render_info(request):
    return render(request, 'info.html')

def render_korzina(request):
    return render(request, 'korzina.html')

def render_politika(request):
    return render(request, 'politika.html')

def render_pravila(request):
    return render(request, 'pravila.html')

def render_pred_pokupka(request):
    return render(request, 'pred_pokupka.html')
