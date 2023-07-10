from django.urls import path
from .views import *
from . import views

app_name="album"
urlpatterns = [
    path('', views.album_read_create),
    path('albums/<int:album_id>', views.album_update_delete),
    path('albums/<int:album_id>/tracks', views.track_read_create),
    path('tracks/<int:track_id>', views.track_update_delete),
    path('tags/<str:tag_name>', views.find_tag),
]