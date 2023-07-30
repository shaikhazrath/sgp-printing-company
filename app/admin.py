from django.contrib import admin
from . models import Product
from django.contrib.auth.models import Group
admin.site.unregister(Group)
admin.site.register(Product)