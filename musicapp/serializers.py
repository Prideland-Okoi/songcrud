from rest_framework import serializers

from .models import *


class ArtisteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'


class SongSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class LyricSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'
