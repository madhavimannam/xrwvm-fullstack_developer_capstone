from django.contrib import admin
from .models import CarMake, CarModel

# Define an inline for CarModel
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

# Define the admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')

# Define the admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
