from django.db import models


#user table 
class User(models.Model):

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    secondary_address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    

    def __str__(self):
        return self.name
    
#products table
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField()
    img = models.ImageField(upload_to='products/', null=True,blank=True)


    def __str__(self):
        return self.name

#sales table
class Sale(models.Model):
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.customer_name} on {self.date.strftime('%Y-%m-%d')}"
    
