from django.urls import path

from world_of_speed_app.core.views import create_profile
from world_of_speed_app.profiles.views import \
    DetailProfileView, EditProfileView, DeleteProfileView


urlpatterns = (
    path('create/', create_profile, name='profile_create'),
    path('details/', DetailProfileView.as_view(), name='profile_details'),
    path('edit/', EditProfileView.as_view(), name='profile_edit'),
    path('delete/', DeleteProfileView.as_view(), name='profile_delete'),
)
