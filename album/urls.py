from django.urls import path
from .views import *
from . import views

app_name="album"
urlpatterns = [
    path('', views.album_read_create),
    path('<int:album_id>', views.album_update_delete),
    path('<int:album_id>/track', views.track_read_create),
    path('track/<int:track_id>', views.track_update_delete),
]