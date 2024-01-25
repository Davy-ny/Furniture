from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPage, name='index'),
    path('living/', views.LivingPage, name='living'),
    path('kitchen_dining/', views.Kitchen_DiningPage, name='kitchen_dining'),
    path('bedroom/', views.BedroomPage, name='bedroom'),
    path('contact/', views.ContactPage, name='contact'),
    path('homeoffice/', views.HomeOfficePage, name='homeoffice'),
    path('Outdoor/', views.OutdoorPage, name='Outdoor')
]