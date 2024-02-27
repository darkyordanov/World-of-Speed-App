from django.urls import include, path

from world_of_speed_app.cars.views import \
    CatalogCarsView, CreateCarView, DeleteCarView, DetailCarView, EditCarView


urlpatterns = (
    path('catalogue/', CatalogCarsView.as_view(), name='catalogue'),
    path('create/', CreateCarView.as_view(), name='car_create'),
    
    path('<int:pk>/', include([
        path('details/', DetailCarView.as_view(), name='car_details'),
        path('edit/', EditCarView.as_view(), name='car_edit'),
        path('delete/', DeleteCarView.as_view(), name='car_delete'),
    ]))
)