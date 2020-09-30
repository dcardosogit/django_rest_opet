from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Serie, Episodio

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

class EpisodioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episodio
        fields = ['episodio_serie','episodio_titulo','episodio_avaliacao']

class SerieSerializer(serializers.HyperlinkedModelSerializer):
    lista_de_episodios = EpisodioSerializer(many=True,source='episodio_set')
    class Meta:
        model = Serie
        fields = ['serie_titulo','serie_temporadas','serie_genero','lista_de_episodios']

