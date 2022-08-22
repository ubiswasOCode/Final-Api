
from django.contrib import admin

from Ecommapp.models import Product, RegisterUser, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(RegisterUser)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
