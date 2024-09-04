from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from django.templatetags.static import static
from . import models
from .models import CartItem,Product


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
    products = Product.objects.all()  # Fetching all products from the database
    return render(request, 'vegetables.html', {'products': products})

def product(request, product_name):
    product = get_object_or_404(Product, name=product_name)  # Fetch product from the database 
    product_img_url = static(product.img)  # Get the image URL from static files
    return render(request, 'product.html', {'product': product, 'img_url': product_img_url})

def add_to_cart(request, product_name):
    if request.method == 'POST':
        product = get_object_or_404(Product, name=product_name)
        quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart')  # Redirect to the cart page after adding the item
    return redirect('vegetables')  # Redirect back to the vegetables page if not a POST request  


def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Assuming you have a user field
    cart_total = sum(item.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)

def update_cart(request):
    if request.method == 'POST':
        for item_id, quantity in request.POST.items():
            if item_id.isdigit():  # Ensure the item_id is valid
                cart_item = get_object_or_404(CartItem, id=item_id)
                cart_item.quantity = quantity
                cart_item.save()
    return redirect('cart')

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







