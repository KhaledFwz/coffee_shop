from django.contrib import admin
from .models import User,Product,Sale
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'age')
    search_fields = ('name', 'email' , 'phone')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')    
    search_fields = ('name', 'category')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date')
    filter_horizontal = ('products',)
    search_fields = ('customer_name',)


