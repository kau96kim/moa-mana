from api.mana.models import Mana, Episode
from rest_framework import serializers


class ManaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="mana-detail")
    is_subscribed = serializers.SerializerMethodField('_is_subscribed')

    def _is_subscribed(self, obj):
        request = self.context['request']
        return True if request.user.profile.manas.filter(pk=obj.pk).exists() else False

    class Meta:
        model = Mana
        fields = ['pk', 'title', 'url', 'is_subscribed']


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ['title', 'order', 'status']
