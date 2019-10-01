from api.mana.serializers import ManaSerializer, EpisodeSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from api.mana.models import Mana, Episode


class ManaViewSet(viewsets.ModelViewSet):
    queryset = Mana.objects.all()
    serializer_class = ManaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def retrieve(self, request, pk=None):
        mana = Mana.objects.get(pk=pk)
        queryset = mana.episode_set.all()
        serializer = EpisodeSerializer(queryset, many=True)
        return Response(serializer.data)


