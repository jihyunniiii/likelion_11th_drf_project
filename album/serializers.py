from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SerializerMethodField(read_only=True)
    tag = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        tracks = instance.tracks.values_list('title', flat=True)
        return tracks
    
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Album
        fields = ['id', 'artist', 'title', 'year_of_release', 'description', 'tracks', 'tag']

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()

    def get_album(self, instance):
        return instance.album.title
    
    class Meta:
        model = Track
        exclude = ['id']
        read_only_fields = ['album']