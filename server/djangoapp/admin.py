from django.contrib import admin
from .models import CarMake,CarModel


# Register your models here.

# CarModelInline class
class CarModelInline (admin.StackedInline):
    model = CarModel
    extra = 3

class CarModelAdmin (admin.ModelAdmin):
    list_display = ['Name', 'DealerID', 'Type']
    list_filter = ['Year']

class CarMakeAdmin (admin.ModelAdmin):
    inline = [CarModelInline]
    list_display = ['Name', 'Description']

# Register models here
admin.site.register (CarMake, CarMakeAdmin)
admin.site.register (CarModel, CarModelAdmin)
