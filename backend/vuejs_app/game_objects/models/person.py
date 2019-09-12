from django.db import models

# Create your models here.
from game_objects.models.default import BaseGameObject


class Person(BaseGameObject):
    """
    Model for all characters, plants and living units
    """
    age = models.FloatField(default=0.0)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    race = models.CharField(max_length=255, default='')
    sex = models.CharField(max_length=255, default='')
