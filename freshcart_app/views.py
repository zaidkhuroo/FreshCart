from django.shortcuts import render, HttpResponse, get_object_or_404
from django.templatetags.static import static
from . import models


# Centralized product data
products_data = {
    'Carrot': {
        'img': 'images/vegetables/carrot.jpg',
        'name': 'Carrot',
        'price': 40,
        'origprice': 50,
        'new': False,
        'sale': True,
        'description': 'Carrots are vibrant, crunchy root vegetables known for their sweet flavor and rich nutritional content. Packed with beta-carotene, which converts to vitamin A in the body, they are essential for good vision, immune function, and skin health. Carrots also provide fiber, antioxidants, and various vitamins and minerals, making them a heart-healthy choice that supports digestion and overall wellness. Whether eaten raw, cooked, or juiced, carrots are a versatile addition to meals, enhancing both flavor and nutrition. Their bright orange color and natural sweetness make them a favorite in both savory and sweet dishes.',
    },
    'Tomato': {
        'img': 'images/vegetables/tomato.jpg',
        'name': 'Tomato',
        'price': 30,
        'origprice': 60,
        'new': False,
        'sale': False,
        'description': 'Tomatoes are vibrant, juicy fruits commonly mistaken for vegetables. They are rich in vitamins A and C, potassium, and antioxidants like lycopene, which may reduce the risk of heart disease and cancer. Tomatoes are versatile, used in various cuisines worldwide, from fresh salads to cooked sauces. Their sweet-tangy flavor enhances dishes like pasta, pizza, and soups. They come in various sizes and colors, including red, yellow, and green, each offering unique culinary uses. Tomatoes are low in calories and high in water content, making them a healthy addition to any diet.',
    },
      'Pumpkin': {
        'img': 'images/vegetables/pumpkin.jpg',
        'name': 'Pumpkin',
        'price': 70,
        'origprice': 110,
        'new': False,
        'sale':True,
        'description': 'Pumpkins are large, round, and vibrant orange fruits often associated with autumn and Halloween. They are packed with nutrients, including vitamins A, C, and E, as well as fiber and antioxidants like beta-carotene, which promotes eye health and boosts the immune system. Pumpkins have a mildly sweet flavor and are incredibly versatile in cooking, used in both savory and sweet dishes. They can be roasted, pureed for soups, or used in pies and bread. Pumpkin seeds are also a nutritious snack, rich in protein and healthy fats. Low in calories and high in vitamins, pumpkins are a nutritious and delicious addition to any meal.',
    },
    'Turnip': {
        'img': 'images/vegetables/turnip.jpg',
        'name': 'Turnip',
        'price': 20,
        'origprice': 40,
        'new': True,
        'sale': False,
        'description': 'Turnips are root vegetables with a slightly sweet and peppery flavor. They are rich in vitamins C and B6, fiber, and essential minerals like potassium and manganese. Turnips are low in calories, making them a great addition to a healthy diet. They can be eaten raw in salads for a crisp texture or cooked in various dishes like soups, stews, and roasts. Both the bulbous root and the leafy greens, known as turnip greens, are edible and nutritious. Turnips are often used in winter dishes and are valued for their versatility and health benefits.',
    },
     'Cocumber': {
        'img': 'images/vegetables/cocumber.jpg',
        'name': 'Cocumber',
        'price': 25,
        'origprice': 45,
        'new': False,
        'sale': False,
        'description': 'Cucumbers are refreshing, hydrating vegetables with a mild, crisp flavor. Composed of about 95% water, they are low in calories and rich in vitamins K and C, as well as potassium. Cucumbers are excellent for hydration and are often used in salads, sandwiches, and as a healthy snack. They can be eaten raw, pickled, or even added to drinks like water or smoothies for a cooling effect. Cucumbers also contain antioxidants and have anti-inflammatory properties, making them beneficial for skin health. Their versatility and nutritional benefits make them a staple in many diets.',
    },
   
     'Onion': {
        'img': 'images/vegetables/onion.jpg',
        'name': 'Onion',
        'price': 18,
        'origprice': 22,
        'new': True,
        'sale': False,
        'description': 'Onions are aromatic vegetables known for their pungent flavor and versatility in cooking. They are rich in vitamins C and B6, folate, and antioxidants like quercetin, which has anti-inflammatory properties. Onions come in various types, including red, white, and yellow, each with a distinct flavor profile. They can be eaten raw in salads, cooked in soups and stews, caramelized, or used as a base in countless dishes. Onions add depth and flavor to meals and are also known for their potential health benefits, including heart health support and immune system boosting.',
    },
     'Potato': {
        'img': 'images/vegetables/potato.jpg',
        'name': 'Potato',
        'price': 30,
        'origprice': 42,
        'new': False,
        'sale': False,
        'description': 'Potatoes are starchy root vegetables that are a staple in many diets worldwide. They are rich in carbohydrates, providing a quick source of energy, and are also a good source of vitamin C, potassium, and fiber. Potatoes can be prepared in numerous ways, including boiling, baking, frying, and roasting. They are incredibly versatile, used in dishes like mashed potatoes, fries, soups, and stews. Despite their simplicity, potatoes are nutritious, and when eaten with the skin, they provide additional fiber and nutrients. They are a comfort food and a dietary staple in many cultures.',
        
    },'Lady-Finger': {
        'img': 'images/vegetables/lady finger.jpg',
        'name': 'Lady-Finger',
        'price': 40,
        'origprice': 53,
        'new': True,
        'sale': False,
        'description': 'Lady Finger, also known as okra, is a green, finger-shaped vegetable with a mild flavor and slimy texture when cooked. It is rich in vitamins C and K, folate, and fiber, making it a nutritious addition to meals. Okra is commonly used in stews, soups, and fried dishes, particularly in Southern and Indian cuisines. It is also known for its mucilaginous quality, which thickens dishes like gumbo. Okra is low in calories and has antioxidant properties, supporting heart health and digestion. Its unique texture and health benefits make it a popular vegetable in various dishes.',
    },
    'Broccoli': {
        'img': 'images/vegetables/broccli.jpg',
        'name': 'Broccoli',
        'price': 60,
        'origprice': 62,
        'new': True,
        'sale': False,
        'description': 'Broccoli is a cruciferous vegetable known for its dense nutritional profile. It is rich in vitamins C, K, and A, as well as fiber, folate, and powerful antioxidants like sulforaphane, which may have cancer-fighting properties. Broccoli can be eaten raw, steamed, roasted, or stir-fried, making it a versatile addition to many dishes. Its slightly bitter taste mellows when cooked, and it pairs well with a variety of flavors. Broccoli is often included in healthy diets due to its low calorie content and potential health benefits, including support for immune function, bone health, and digestion.',
    },
    'Cabbage': {
        'img': 'images/vegetables/cabbage.jpg',
        'name': 'Cabbage',
        'price': 30,
        'origprice': 42,
        'new': False,
        'sale': False,
        'description': 'Cabbage is a leafy green, red, or white vegetable that belongs to the Brassica family. It is rich in vitamins C and K, fiber, and antioxidants like anthocyanins, especially in red cabbage. Cabbage can be eaten raw, fermented, or cooked in a variety of ways, including boiling, sautéing, and roasting. It is commonly used in salads, slaws, and soups. Fermented cabbage, known as sauerkraut or kimchi, is valued for its probiotic benefits. Cabbage is low in calories and has potential health benefits, including improved digestion, heart health, and reduced inflammation.',
    },
      'Brinjal': {
        'img': 'images/vegetables/brinjal.jpg',
        'name': 'Brinjal',
        'price':26,
        'origprice': 35,
        'new': False,
        'sale': True,
        'description': 'Brinjal, also known as eggplant, is a glossy purple vegetable with a spongy texture. It is rich in dietary fiber, vitamins B1 and B6, and antioxidants like nasunin, which is found in its skin and has potential brain-protective properties. Eggplant is versatile in cooking, absorbing flavors well in dishes like curries, stews, and grilled preparations. It can be baked, roasted, grilled, or sautéed, and is often used in Mediterranean and Asian cuisines. Brinjal is low in calories and has been linked to heart health benefits, making it a nutritious and flavorful addition to meals.',
    },
        'Cauliflower': {
        'img': 'images/vegetables/cauliflower.jpg',
        'name': 'Cauliflower',
        'price': 40,
        'origprice': 48,
        'new': False,
        'sale': False,
        'description': 'Cauliflower is a cruciferous vegetable known for its mild flavor and versatility. It is packed with vitamins C and K, fiber, and antioxidants like glucosinolates, which may help protect against cancer. Cauliflower can be eaten raw, steamed, roasted, or mashed, and is often used as a low-carb substitute for grains and potatoes in dishes like cauliflower rice and pizza crust. Its neutral taste makes it adaptable to various flavors and cooking methods. Cauliflower is low in calories and high in nutrients, making it a popular choice for health-conscious diets.',
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


