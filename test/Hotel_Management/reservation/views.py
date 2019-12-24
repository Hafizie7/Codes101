from django.shortcuts import render

# Create your views here.

from .models import *

def index(request):
    return render(request, 'index.html')

def display_SingleBed(request):
    items = SingleBed.objects.all()
    context = {
        'items': items,
        'header' : 'SingleBed'
    }
    return render(request, 'index.html', context)

def display_Double_bed(request):
    items = Double_bed.objects.all()
    context = {
        'items': items,
        'header' : 'Double_bed'
    }
    return render(request, 'index.html', context)

def display_Customer(request):
    items = Customer.objects.all()
    context = {
        'items': items,
        'header' : 'Customer'
    }
    return render(request, 'customer.html', context)
