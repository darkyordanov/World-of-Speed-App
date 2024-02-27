from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('world_of_speed_app.core.urls')),
    path('car/', include('world_of_speed_app.cars.urls')),
    path('profile/', include('world_of_speed_app.profiles.urls')),
]
