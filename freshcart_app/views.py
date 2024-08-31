from django.shortcuts import render, HttpResponse, get_object_or_404
from . import models

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


def vegetables(request): 
    product1=models.Vegetables()
    product1.img='static/images/img-pro-01.jpg'
    product1.name='Carrot'
    product1.price= '40'
    product1.origprice= '50'
    product1.new=False
    product1.sale=True
    
    product2=models.Vegetables()
    product2.img='static/images/img-pro-02.jpg'
    product2.name='Tomato'
    product2.price= '30'
    product2.origprice= '60'
    product2.new=False
    product2.sale=False
    
    products=[product1,product2]
    return render(request,'vegetables.html', {'products':products})

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
def product(request): 
    return render(request,'product.html')
def login(request): 
    return render(request,'login.html')


def product(request, product_name):
    # Dummy data to match product_name
    products_data = {
        'Carrot': {
            'img': 'static/images/img-pro-01.jpg',
            'name': 'Carrot',
            'price': 40,
            'origprice': 50,
            'new': False,
            'sale': True,
            'description': 'Fresh Carrots are nutrient-dense...',
        },
        'Tomato': {
            'img': 'static/images/img-pro-02.jpg',
            'name': 'Tomato',
            'price': 30,
            'origprice': 60,
            'new': False,
            'sale': False,
            'description': 'Fresh Tomatoes are juicy and rich...',
        }
    }
    
    product = products_data.get(product_name)
    
    if not product:
        return HttpResponse("Product not found.", status=404)
    
    return render(request, 'product.html', {'product': product})

def fruits(request):
    return render(request, 'fruits.html')

def dairy(request):
    return render(request, 'dairy.html')
