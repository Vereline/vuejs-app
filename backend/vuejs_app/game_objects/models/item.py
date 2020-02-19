from django.db import models

# Create your models here.
from game_objects.models.default import BaseGameObject


class Item(BaseGameObject):
    """
    In-game items, such as items in inventory, in locations
    """
    weight = models.FloatField(default=0.0, help_text='In kilos')
    price = models.FloatField(default=0.0)
    abilities = None
