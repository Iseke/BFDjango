from django.contrib import admin
from mysite.main.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


admin.site.register(Category)