from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        serializer = TrackSerializer(instance.tracks, many=True)
        return serializer.data

    class Meta:
        model = Album
        fields = ['id', 'artist', 'title', 'year_of_release', 'description', 'tracks']

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()

    def get_album(self, instance):
        return instance.album.title
    
    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['album']