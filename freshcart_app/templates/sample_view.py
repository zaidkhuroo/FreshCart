from django.shortcuts import render,redirect, get_object_or_404
from django.templatetags.static import static
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import CreateUser, LoginUser
from .models import CartItem,Product,WishlistItem
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView




# CART START

@login_required(login_url='login')
def add_to_wishlist(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    
    # Get quantity from POST data, default to 1 if not provided
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if the item already exists in the user's cart
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    
    if created:
        wishlist_item.quantity = quantity  # Set quantity if item is newly added
    else:
        wishlist_item.quantity += quantity  # Update quantity if already exists
    
    # Calculate total price and save the cart item
    wishlist_item.save()
    
    messages.success(request, f'{product.name} added to your wishlist.')
    return redirect('wishlist')


@login_required(login_url='login')
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    context = {
        'wishlist_items':wishlist_items,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def update_wishlist(request):
    if request.method == 'POST':
        for item_id, quantity in request.POST.items():
            if item_id.isdigit():  # Ensure the item_id is valid
                wishlist_item = get_object_or_404(WishlistItem, id=item_id)
                wishlist_item.quantity = quantity
                wishlist_item.save()
    return redirect('wishlist')


@login_required(login_url='login')
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    wishlist_item.delete()
    return redirect('wishlist')
#wishlist End

    


