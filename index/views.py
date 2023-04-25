from django.shortcuts import render
from .models import WorkingHours, OurWorks, PhoneNumber, ServicesAndPrices
from django.views.generic import DetailView

def index(request):
    hours = WorkingHours.objects.all()
    return render(request, 'index/index.html', {'hours': hours})

def our_works(request):
    our_works = OurWorks.objects.order_by('date')
    return render(request, 'index/our_works.html', {'our_works': our_works})

class WorksDetailView(DetailView):
    model = OurWorks
    template_name = 'index/detail_view.html'
    context_object_name = 'our_work'

def contacts(request):
    phone_number = PhoneNumber.objects.first()
    return render(request, 'index/contacts.html', {'phone_number': phone_number})

def prices(request):
    services = ServicesAndPrices.objects.all()
    return render(request, 'index/prices.html', {'services': services})
