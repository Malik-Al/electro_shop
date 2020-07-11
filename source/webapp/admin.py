from django.contrib import admin
from webapp.models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category']
    list_filter = ['name', 'category']
    fields = ['name', 'description', 'category', 'amount', 'price']
    readonly_fields = ['amount', 'price']

admin.site.register(Product, ProductAdmin)