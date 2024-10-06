from django.shortcuts import render,redirect, get_object_or_404
from django.templatetags.static import static
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import CreateUser, LoginUser
from .models import CartItem,Product,WishlistItem,Fruits
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin


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


fruits_data = {
 'Apple': {
    'img': 'images/fruits/apple.jpg',
    'name': 'Apple',
    'price': 50,
    'origprice': 60,
    'new': True,
    'sale': True,
    'description': 'Apples are a highly nutritious fruit, rich in dietary fiber, vitamin C, and various antioxidants. They are known for promoting heart health, aiding in digestion, and supporting weight management. Apples come in a variety of flavors, ranging from sweet to tangy, and are enjoyed both raw and cooked. Their versatility makes them a popular choice in everything from snacks to desserts, salads, and juices. Eating apples regularly is linked to a reduced risk of chronic diseases like heart disease and diabetes. This fruit is a favorite for its convenience, taste, and impressive health benefits.',
},
    'Banana': {
        'img': 'images/fruits/banana.jpg',
        'name': 'Banana',
        'price': 20,
        'origprice': 25,
        'new': True,
        'sale': False,
        'description': 'Bananas are one of the most widely consumed fruits in the world, known for their creamy texture and naturally sweet flavor. Packed with essential nutrients such as potassium, vitamin C, and dietary fiber, bananas provide quick energy and help regulate blood pressure. They are often enjoyed on their own, added to smoothies, or used in baking. Bananas are also easy to digest, making them a great snack for all ages. With their high fiber content, bananas promote digestive health and are an excellent choice for maintaining a balanced diet.',
    },
    'Cherry': {
        'img': 'images/fruits/cherry.jpg',
        'name': 'Cherry',
        'price': 80,
        'origprice': 90,
        'new': False,
        'sale': True,
        'description': 'Cherries are small, round fruits that are bursting with flavor and packed with nutrients. They are a rich source of antioxidants, including vitamin C and anthocyanins, which have been shown to reduce inflammation and improve heart health. Cherries are often eaten fresh, but they can also be used in jams, desserts, and smoothies. Their deep red color and sweet-tart taste make them a favorite for both snacking and cooking. Cherries are also known to promote better sleep due to their melatonin content, making them a healthful and delicious addition to any diet.',
    },
    'Dragon Fruit': {
        'img': 'images/fruits/dragon.jpg',
        'name': 'Dragon Fruit',
        'price': 120,
        'origprice': 140,
        'new': True,
        'sale': True,
        'description': 'Dragon fruit, also known as pitaya, is a tropical fruit with a striking appearance and a mild, sweet flavor. It is rich in antioxidants, including vitamin C, and contains fiber, making it beneficial for digestion. The flesh of the dragon fruit can be white or red, dotted with small, edible seeds. Dragon fruit is often enjoyed on its own, in smoothies, or as a topping for yogurt and salads. Its high water content makes it a hydrating snack, and its vibrant color adds an exotic touch to any meal. This superfood is both nutritious and refreshing.',
    },
    'Grapes': {
        'img': 'images/fruits/grapes.jpg',
        'name': 'Grapes',
        'price': 60,
        'origprice': 70,
        'new': False,
        'sale': True,
        'description': 'Grapes are small, juicy fruits that come in various colors including green, red, and purple. They are packed with vitamins C and K, as well as antioxidants like resveratrol, which is beneficial for heart health. Grapes are enjoyed fresh as a snack or can be used to make juice, wine, and jams. Their natural sweetness and versatility make them a popular ingredient in salads, desserts, and beverages. Grapes also provide hydration and support immune health, making them an excellent addition to any diet. They are a perfect blend of taste and nutrition.',
    },
    'Kiwi': {
        'img': 'images/fruits/kiwi.jpg',
        'name': 'Kiwi',
        'price': 45,
        'origprice': 50,
        'new': True,
        'sale': False,
        'description': 'Kiwi is a small, fuzzy fruit with vibrant green flesh and a unique sweet-tart flavor. It is loaded with vitamin C, more than most other fruits, and also provides fiber, vitamin K, and antioxidants. Kiwis are known for their ability to boost immune health, improve digestion, and promote healthy skin. They are often eaten fresh, sliced into salads, or added to smoothies. Their exotic appearance and refreshing taste make them a popular choice in fruit salads and desserts. Kiwi is a nutrient-dense fruit that offers numerous health benefits in every bite.',
    },
    'Litchi': {
        'img': 'images/fruits/litchee.jpg',
        'name': 'Litchi',
        'price': 90,
        'origprice': 100,
        'new': False,
        'sale': False,
        'description': 'Litchi, also known as lychee, is a tropical fruit with a sweet, floral flavor and a juicy texture. It is a rich source of vitamin C and antioxidants, which support immune function and skin health. The translucent flesh of the litchi is enclosed in a rough, red skin that is peeled away before eating. Litchis are often enjoyed fresh or added to desserts, beverages, and fruit salads. They are prized for their refreshing taste and delicate fragrance. Litchis are not only delicious but also packed with nutrients that contribute to overall well-being.',
    },
    'Mango': {
        'img': 'images/fruits/mango.jpg',
        'name': 'Mango',
        'price': 100,
        'origprice': 120,
        'new': True,
        'sale': True,
        'description': 'Mangoes are often referred to as the "king of fruits" due to their delicious flavor and rich nutritional content. They are packed with vitamins A and C, as well as fiber and antioxidants. Mangoes come in many varieties, each with a unique taste ranging from sweet to tangy. They can be eaten fresh, added to smoothies, or used in a variety of dishes such as salsas and desserts. Mangoes are also known for their skin health benefits and digestive support. This tropical fruit is a favorite worldwide for its juicy, golden flesh and irresistible taste.',
    },
    'Orange': {
        'img': 'images/fruits/orange.jpg',
        'name': 'Orange',
        'price': 40,
        'origprice': 50,
        'new': False,
        'sale': True,
        'description': 'Oranges are one of the most popular citrus fruits, known for their bright flavor and high vitamin C content. In addition to vitamin C, oranges provide fiber, potassium, and antioxidants. They are commonly enjoyed fresh, juiced, or as part of salads and desserts. Oranges help boost the immune system, improve skin health, and support heart health. Their tangy sweetness makes them a refreshing snack, especially in summer. Whether eaten on their own or added to dishes, oranges bring a burst of flavor and nutrition to any meal, making them a staple in many households.',
    },
    'Papaya': {
        'img': 'images/fruits/papaya.jpg',
        'name': 'Papaya',
        'price': 35,
        'origprice': 40,
        'new': True,
        'sale': False,
        'description': 'Papaya is a tropical fruit known for its vibrant orange flesh and sweet, musky flavor. It is rich in vitamins C and A, as well as digestive enzymes like papain, which help improve digestion. Papayas are often eaten fresh, blended into smoothies, or used in fruit salads. They are also popular in savory dishes, especially in tropical cuisines. Papaya promotes digestive health, supports the immune system, and provides hydration due to its high water content. This nutrient-dense fruit is a delicious and refreshing way to boost your health with every bite.',
    },
    'Pineapple': {
        'img': 'images/fruits/pineapple.jpg',
        'name': 'Pineapple',
        'price': 85,
        'origprice': 95,
        'new': False,
        'sale': True,
        'description': 'Pineapple is a tropical fruit with a sweet and tangy flavor, often used in a variety of dishes from salads to desserts. It is packed with vitamin C, manganese, and digestive enzymes like bromelain, which aid in digestion. Pineapple is enjoyed fresh, juiced, or as a topping for pizzas and desserts. Its high water content makes it a hydrating snack, while its unique flavor profile makes it a versatile ingredient in both sweet and savory recipes. Pineapple is not only delicious but also a great source of important nutrients that support overall health.',
    },
    'Strawberry': {
        'img': 'images/fruits/strawberry.jpg',
        'name': 'Strawberry',
        'price': 75,
        'origprice': 85,
        'new': True,
        'sale': True,
        'description': 'Strawberries are a popular berry known for their bright red color, juicy texture, and sweet flavor. They are rich in vitamin C, manganese, and antioxidants, making them a highly nutritious snack. Strawberries are commonly eaten fresh, blended into smoothies, or added to desserts like cakes and pies. They are also a favorite for making jams and sauces. In addition to their delicious taste, strawberries are known for supporting heart health, reducing inflammation, and promoting healthy skin. This versatile fruit is enjoyed around the world in a variety of dishes and forms.',
    }
}


@login_required(login_url='login')   
def fruits(request): 
    fruit_products = list(fruits_data.values()) 
    # products = Fruits.objects.all()  # Fetching all products from the database
    print(fruit_products)
    return render(request, 'fruits.html', {'fruit_products': fruit_products})

@login_required(login_url='login')
def product(request, product_name):
    product = get_object_or_404(Product, name=product_name)  # Fetch product from the database 
    product_img_url = static(product.img)  # Get the image URL from static files
    return render(request, 'product.html', {'product': product, 'img_url': product_img_url})


# CART

@login_required(login_url='login')
def add_to_cart(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    
    # Get quantity from POST data, default to 1 if not provided
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if the item already exists in the user's cart
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    
    if created:
        cart_item.quantity = quantity  # Set quantity if item is newly added
    else:
        cart_item.quantity += quantity  # Update quantity if already exists
    
    # Calculate total price and save the cart item
    cart_item.save()
    
    messages.success(request, f'{product.name} added to your cart.')
    return redirect('cart')



@login_required(login_url='login')
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.total_price for item in cart_items)

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
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
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

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'  # Create this template for the change password page
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')  # Redirect after successful password change
    success_message = "Your password was successfully updated!"
    
    

# CART START

@login_required(login_url='login')
def add_to_wishlist(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    
    quantity = int(request.POST.get('quantity', 1))
    
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
 
    wishlist_item.quantity = quantity  # Set quantity if item is newly added
  
    wishlist_item.save()
    
    messages.success(request, f'{product.name} added to your wishlist.')
    return redirect('wishlist')


@login_required(login_url='login')
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items  # Pass actual data
    }
    return render(request, 'wishlist.html', context)


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

    



