from django.contrib import admin
from .models import UserProfile,Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price','user')
    prepopulated_fields = {'slug': ('item_name',)} 

admin.site.register(UserProfile)
admin.site.register(Product,ProductAdmin)