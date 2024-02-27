from django.contrib import admin

from world_of_speed_app.profiles.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass