from django.contrib import admin

from .models import Car
from .models import Brand

class adminCar(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo', )
    search_fields = ('model', )

admin.site.register(Car, adminCar, )

class adminBrand(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(Brand, adminBrand, )
