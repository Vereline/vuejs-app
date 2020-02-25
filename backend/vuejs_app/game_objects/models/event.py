from django.db import models

# Create your models here.
from game_objects.models.item import Item
from game_objects.models.person import Person
from game_objects.models.place import Place
from game_objects.models.default import BaseGameObject
from game_objects.managers import EventManager, AbilityManager


class Event(BaseGameObject):
    """
    In-game events, accidents, story points
    """
    persons = models.ManyToManyField(Person, related_name='person_events', null=True)
    condition = models.CharField(max_length=255, default='')
    place = models.ForeignKey(Place, related_name='place_events', on_delete=models.DO_NOTHING, null=True)
    items = models.ManyToManyField(Item, related_name='events', null=True)

    objects = EventManager()


class Ability(BaseGameObject):
    """
    Spell, perk etc, all things with balance
    """
    persons = models.ManyToManyField(Person, related_name='person_abilities', null=True)
    power = models.CharField(max_length=255, default='')
    stamina_points = models.IntegerField(default=0, null=False)

    objects = AbilityManager()
