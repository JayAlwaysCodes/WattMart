from django.contrib import admin

# Category

from .models import Category, Item


admin.site.register(Category)
admin.site.register(Item)