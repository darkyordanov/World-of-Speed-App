from django.contrib import admin

from world_of_speed_app.cars.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass