from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Breed(models.Model):
    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    SIZE_CHOICE = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'large'),
    )
    name = models.CharField(max_length=50, blank=False, default='', unique=True)
    size = models.CharField(
        max_length=2,
        choices=SIZE_CHOICE,
        default=SMALL,
    )
    friendliness = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    trainability = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    sheddingamount = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    exerciseneeds = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Dog(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=50, blank=False, default='', unique=True)
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed, 
        on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    color = models.CharField(max_length=50, blank=False, default='')
    favoriteFood = models.CharField(max_length=50, blank=False, default='')
    favoriteToy = models.CharField(max_length=50, blank=False, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name