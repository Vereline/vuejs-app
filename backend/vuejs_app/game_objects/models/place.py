from django.db import models

# Create your models here.
from game_objects.models.default import BaseGameObject
from game_objects.models.person import Person
from game_objects.managers import PlaceManager


class Place(BaseGameObject):
    """
    Models of locations
    """
    size = models.CharField(max_length=255, default='', help_text='Size of location or something special and unique')
    flora = models.ManyToManyField(Person, related_name='flora_places')
    fauna = models.ManyToManyField(Person, related_name='fauna_places')

    objects = PlaceManager()
