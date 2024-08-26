from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request): 
    return render(request,'index.html')
def about(request): 
    return render(request,'about.html')
def checkout(request): 
    return render(request,'checkout.html')
def contact(request): 
    return render(request,'contact-us.html')
def gallery(request): 
    return render(request,'gallery.html')
def account(request): 
    return render(request,'my-account.html')
def wish(request): 
    return render(request,'wishlist.html')
def cart(request): 
    return render(request,'cart.html')