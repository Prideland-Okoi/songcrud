from rest_framework import viewsets
from musicapp.serializers import ArtisteSerilizer
from .models import Artiste, Lyric, Song
from .serializers import ArtisteSerilizer, SongSerilizer, LyricSerilizer


class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class  = ArtisteSerilizer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class  = SongSerilizer


class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class  = LyricSerilizer
