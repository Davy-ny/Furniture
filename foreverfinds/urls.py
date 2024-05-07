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
    path('cart/', views.CartPage, name='cart'),
    path('checkout/', views.CheckoutPage, name='checkout'),
    path('Outdoor/', views.OutdoorPage, name='Outdoor'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order')
]