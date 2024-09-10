from django.shortcuts import render,redirect, get_object_or_404
from django.templatetags.static import static
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import CreateUser, LoginUser
from .models import CartItem,Product
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
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

@login_required(login_url='login')   
def vegetables(request): 
    products = Product.objects.all()  # Fetching all products from the database
    return render(request, 'vegetables.html', {'products': products})
@login_required(login_url='login')
def product(request, product_name):
    product = get_object_or_404(Product, name=product_name)  # Fetch product from the database 
    product_img_url = static(product.img)  # Get the image URL from static files
    return render(request, 'product.html', {'product': product, 'img_url': product_img_url})
@login_required(login_url='login')
def add_to_cart(request, product_name):
    if request.method == 'POST':
        product = get_object_or_404(Product, name=product_name)
        quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart')  # Redirect to the cart page after adding the item
    return redirect('vegetables')  # Redirect back to the vegetables page if not a POST request  

@login_required(login_url='login')
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Assuming you have a user field
    cart_total = sum(item.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)
@login_required(login_url='login')
def update_cart(request):
    if request.method == 'POST':
        for item_id, quantity in request.POST.items():
            if item_id.isdigit():  # Ensure the item_id is valid
                cart_item = get_object_or_404(CartItem, id=item_id)
                cart_item.quantity = quantity
                cart_item.save()
    return redirect('cart')
@login_required(login_url='login')
def fruits(request): 
    return render(request,'fruits.html')
@login_required(login_url='login')
def dairy(request): 
    return render(request,'dairy.html')
@login_required(login_url='login')
def about(request): 
    return render(request,'about.html')
@login_required(login_url='login')
def checkout(request): 
    return render(request,'checkout.html')

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

       
        # Send email
        try:
            send_mail(
                f"Message from {name}: {subject}",
                message,
                email,  # Sender's email
                [settings.EMAIL_HOST_USER],  # Recipient email
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, "Failed to send message.")

        return redirect('contact')  # Redirect after successful form submission
    
    return render(request, 'contact-us.html')

@login_required(login_url='login')
def account(request): 
    return render(request,'my-account.html')
def wish(request): 
    return render(request,'wishlist.html')
@login_required(login_url='login')
def cart(request): 
    return render(request,'cart.html')



def login(request):
    form=LoginUser()
    if request.method == 'POST':
        form =LoginUser(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username') 
            password=request.POST.get('password')
            user= authenticate(request,username=username,password=password) 
            if user is not None:
                auth.login(request,user)
                return redirect ('home')
    context={'form': form}
    return render(request,'login.html', context=context)            
                
def register(request):
    form=CreateUser() 
    if request.method == 'POST':
        form =CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form': form}
    return render(request,'register.html', context=context)            
    
def logout(request):
    auth.logout(request)
    return redirect('login')






