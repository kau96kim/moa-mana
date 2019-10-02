from api.mana.serializers import ManaSerializer, EpisodeSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from api.mana.models import Mana, Episode


class ManaViewSet(viewsets.ModelViewSet):
    serializer_class = ManaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    queryset = Mana.objects.all()

    def retrieve(self, request, pk=None):
        mana = Mana.objects.get(pk=pk)
        queryset = mana.episode_set.all().order_by('-order')
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = EpisodeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EpisodeSerializer(queryset, many=True)
        return Response(serializer.data)
