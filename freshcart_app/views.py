from django.shortcuts import render, HttpResponse, get_object_or_404
from django.templatetags.static import static
from . import models


# Centralized product data
products_data = {
    'Carrot': {
        'img': 'images/img-pro-01.jpg',
        'name': 'Carrot',
        'price': 40,
        'origprice': 50,
        'new': False,
        'sale': True,
        'description': 'Fresh Carrots are nutrient-dense...',
    },
    'Tomato': {
        'img': 'images/img-pro-02.jpg',
        'name': 'Tomato',
        'price': 30,
        'origprice': 60,
        'new': False,
        'sale': False,
        'description': 'Fresh Tomatoes are juicy and rich...',
    },
    'Turnip': {
        'img': 'images/img-pro-03.jpg',
        'name': 'Turnip',
        'price': 20,
        'origprice': 34,
        'new': True,
        'sale': False,
        'description': 'Fresh Turnips are juicy and rich...',
    },
     'Cocumber': {
        'img': 'images/img-pro-04.jpg',
        'name': 'Cocumber',
        'price': 10,
        'origprice': 22,
        'new': True,
        'sale': False,
        'description': 'Fresh Turnips are juicy and rich...',
    },
}
    
def vegetables(request): 
    products = list(products_data.values())  # Extracting all products for display
    return render(request, 'vegetables.html', {'products': products})

def product(request, product_name):
    products = list(products_data.values()) 
    product = products_data.get(product_name)
    
    if not product:
        return HttpResponse("Product not found.", status=404)
    product['img'] = static(product['img'])
    
    return render(request, 'product.html', {'product': product})


# Create your views here.
def home(request): 
    product1=models.home_page_categories() #product1 is an object of class home_page_categories
    product1.name='Vegetables'
    product1.img='static/images/categories_img_01.jpg'
    product1.url='vegetables'
    product2=models.home_page_categories() #product1 is an object of class home_page_categories
    product2.name='Fruits'
    product2.img='static/images/categories_img_02.jpg'
    product2.url='fruits'
    product3=models.home_page_categories() #product1 is an object of class home_page_categories
    product3.name='Dairy'
    product3.img='static/images/categories_img_03.jpg'
    product3.url='dairy'
    
    products=[product1,product2,product3]
    return render(request,'index.html', {'products':products})


def fruits(request): 
    return render(request,'fruits.html')
def dairy(request): 
    return render(request,'dairy.html')
def about(request): 
    return render(request,'about.html')
def checkout(request): 
    return render(request,'checkout.html')
def contact(request): 
    return render(request,'contact-us.html')
def account(request): 
    return render(request,'my-account.html')
def wish(request): 
    return render(request,'wishlist.html')
def cart(request): 
    return render(request,'cart.html')

def login(request): 
    return render(request,'login.html')


