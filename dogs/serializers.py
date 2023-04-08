
from rest_framework import serializers
from .models import Dog
from .models import Breed


class DogSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
    gender = serializers.ChoiceField(
        choices=Dog.GENDER_CHOICES)
    class Meta:
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favoriteFood',
            'favoriteToy',
        )
        model = Dog

class BreedSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(
        choices=Breed.SIZE_CHOICE)
    class Meta:
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds',
        )
        model = Breed
        