from django.shortcuts import render
from .models import *


def IndexPage(request):
    return render(request, 'foreverfinds/index.html')

def LivingPage(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'foreverfinds/livingroom.html', context)

def Kitchen_DiningPage(request):
    return render(request, 'foreverfinds/diningroom.html')

def BedroomPage(request):
    return render(request, 'foreverfinds/bedroom.html')

def ContactPage(request):
    return render(request, 'foreverfinds/contact_us.html')

def HomeOfficePage(request):
    return render(request, 'foreverfinds/homeoffice.html')

def OutdoorPage(request):
    return render(request, 'foreverfinds/outdoor.html')

def CheckoutPage(request):
    context = {}
    return render(request, 'foreverfinds/checkout.html', context)

def CartPage(request):
    context = {}
    return render(request, 'foreverfinds/cart.html', context)