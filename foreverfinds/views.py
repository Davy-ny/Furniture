from django.shortcuts import render


def IndexPage(request):
    return render(request, 'index.html')

def LivingPage(request):
    return render(request, 'livingroom.html')

def Kitchen_DiningPage(request):
    return render(request, 'diningroom.html')

def BedroomPage(request):
    return render(request, 'bedroom.html')

def ContactPage(request):
    return render(request, 'contact_us.html')

def HomeOfficePage(request):
    return render(request, 'homeoffice.html')

def OutdoorPage(request):
    return render(request, 'outdoor.html')