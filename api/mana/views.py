from api.mana.serializers import ManaSerializer, EpisodeSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from api.mana.models import Mana


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

    def update(self, request, pk=None):
        mana = Mana.objects.get(pk=pk)
        self.request.user.profile.manas.add(mana)
        queryset = mana

        serializer = ManaSerializer(queryset, many=False, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        mana = Mana.objects.get(pk=pk)
        self.request.user.profile.manas.remove(mana)
        queryset = mana

        serializer = ManaSerializer(queryset, many=False, context={'request': request})
        return Response(serializer.data)


class SubscribedManaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ManaSerializer

    def get_queryset(self):
        return self.request.user.profile.manas.all()

