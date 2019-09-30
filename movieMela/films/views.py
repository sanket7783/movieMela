from django.shortcuts import render
from .models import Films
from django.contrib.auth.models import User
from rest_framework import generics, filters, viewsets
from .serializers import FilmsSerializer, UserSerializer


class FilmsViewSet(generics.ListCreateAPIView):
    search_fields = ['name', 'genre']
    filter_backends = (filters.SearchFilter,)

    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

class FilmsViewSetDetail(generics.RetrieveUpdateDestroyAPIView):

  queryset = Films.objects.all()
  serializer_class = FilmsSerializer

class UserProfileViewSet(generics.ListCreateAPIView):

  serializer_class = UserSerializer
  queryset = User.objects.all()




