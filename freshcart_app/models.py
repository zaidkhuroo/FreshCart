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
    
    
class Product(models.Model):
    name = models.CharField(max_length=100) #primary key
    img = models.ImageField(upload_to='images/vegetables/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    origprice = models.DecimalField(max_digits=10, decimal_places=2)
    new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)  # Optional URL field

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        return ((self.origprice - self.price) / self.origprice) * 100

    @property
    def is_discounted(self):
        return self.price < self.origprice
    
class CartItem(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name