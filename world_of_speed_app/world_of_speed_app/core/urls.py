from django.urls import path

from world_of_speed_app.core.views import index


urlpatterns = (
    path('', index, name='index'),
)
