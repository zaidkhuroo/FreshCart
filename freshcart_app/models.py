from django.db import models

# Create your models here.
class home_page_categories:
    id:int
    name:str
    img:str
    url:str
    
class Vegetables:
    id:int
    img:str
    name:str
    price:int
    orgprice:int
    url:str
    sale:bool
    new:bool