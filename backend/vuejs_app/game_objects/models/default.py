from django.db import models

# Create your models here.
from default.models import TimestampedModel


class BaseGameObject(TimestampedModel):
    """
    Base model for all in-game objects, such as persons, items, locations etc
    """
    name = models.CharField(max_length=255, default='', null=False)
    type = models.CharField(max_length=255, default='', null=False)
    description = models.TextField()

    def __str__(self):
        return '{} #{}: {}'.format(self.__name__, self.id, self.name)

    class Meta:

        abstract = True
