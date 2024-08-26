from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about', views.about, name='about'), 
    path('checkout', views.checkout, name='checkout'), 
    path('contact', views.contact, name='contact'), 
    path('gallery', views.gallery, name='gallery'), 
    path('account', views.account, name='account'), 
    path('wish', views.wish, name='wish'), 
    path('cart', views.cart, name='cart'), 
]