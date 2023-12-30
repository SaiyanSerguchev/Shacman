from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from main.models import Truck

def index(request):
    truck = Truck.objects.all
    context = {
        'tr' : truck
    }
    return render(request, 'main/index.html', context)

class TrucksDetailView(DetailView):
    model=Truck
    template_name='main/details_view.html'
    context_object_name = 'truck'