from django.db import models

# Create your models here.
from game_objects.models.item import Item
from game_objects.models.person import Person
from game_objects.models.place import Place
from game_objects.models.default import BaseGameObject


class Event(BaseGameObject):
    """
    In-game events, accidents, story points
    """
    persons = models.ManyToManyField(Person, related_name='person_events')
    condition = models.CharField(max_length=255, default='')
    place = models.ForeignKey(Place, related_name='place_events', on_delete=models.DO_NOTHING, null=True)
    items = models.ManyToManyField(Item, related_name='events')


class Ability(BaseGameObject):
    """
    Spell, perk etc, all things with balance
    """
    pass
