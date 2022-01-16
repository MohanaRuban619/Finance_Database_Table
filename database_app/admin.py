from django.contrib import admin
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
from .models import Customers


admin.site.register(Customers)
