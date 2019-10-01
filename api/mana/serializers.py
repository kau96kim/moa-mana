from api.mana.models import Mana, Episode
from rest_framework import serializers


class ManaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="mana-detail")

    class Meta:
        model = Mana
        fields = ['pk', 'title', 'link', 'url']


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ['title', 'order', 'link', 'status', 'mana']
