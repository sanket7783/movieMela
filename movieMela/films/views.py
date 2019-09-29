from django.shortcuts import render
from .models import Films
from rest_framework import generics, filters
from .serializers import FilmsSerializer


class FilmsViewSet(generics.ListCreateAPIView):
    search_fields = ['name', 'genre']
    filter_backends = (filters.SearchFilter,)

    queryset = Films.objects.all()
    serializer_class = FilmsSerializer




