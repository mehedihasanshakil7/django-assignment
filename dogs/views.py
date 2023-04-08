from django.shortcuts import render
from rest_framework import generics

from .models import Dog
from .models import Breed
from dogs.serializers import DogSerializer
from dogs.serializers import BreedSerializer

class ListDogs(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-list'


class DetailDog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-detail'


class ListBreeds(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-list'


class DetailBreed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-detail'