from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about', views.about, name='about'), 
    path('checkout', views.checkout, name='checkout'), 
    path('contact', views.contact, name='contact'),  
    path('account', views.account, name='account'), 
    path('wish', views.wish, name='wish'), 
    path('cart', views.cart, name='cart'), 
    path('product', views.product, name='product'), 
    path('vegetables', views.vegetables, name='vegetables'), 
    path('dairy', views.dairy, name='dairy'), 
    path('fruits', views.fruits, name='fruits'), 
    path('login', views.login, name='login'), 
    path('logout', views.logout, name='logout'), 
    path('register', views.register, name='register'), 
    path('product/<str:product_name>/', views.product, name='product'),
    path('add_to_cart/<str:product_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
]