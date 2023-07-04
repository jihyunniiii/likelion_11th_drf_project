from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Album
from .serializers import AlbumSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
def album_list_create(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        
@api_view(['GET', 'PATCH', 'DELETE'])
def album_detail_update_delete(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        album.delete()
        data = {
            'deleted_album':album_id
        }
        return Response(data)