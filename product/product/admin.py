from django.contrib import admin
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','color', 'price')
    list_filter = (('color', DropdownFilter),)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)