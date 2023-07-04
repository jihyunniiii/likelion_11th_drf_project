from django.urls import path
from .views import *
from . import views

app_name="album"
urlpatterns = [
    path('', views.album_list_create),
    path('<int:album_id>', views.album_detail_update_delete),
]