from django.db import models

# Create your models here.


class Ingredient(models.Model):
    UNITS = (
        ('tsp', 'teaspoon',),
        ('tbl', 'tablespoon'),
        ('c', 'cup'),
        ('quart', 'qt'),
        ('gallon', 'gal'),
        ('milliliter', 'ml'),
        ('liter', 'l'),
        ('deciliter', 'dl'),

        ('lb', 'pound'),
        ('oz', 'ounce'),
        ('g', 'gram'),
        ('kg', 'kilogram'),

        ('mm', 'millimeter'),
        ('cm', 'centimeter'),
        ('m', 'meter'),
        ('in', 'inch'),
    )

    name = models.CharField(default='', max_length=255)
    amount = models.PositiveIntegerField(default=0, null=False)
    unit = models.CharField(choices=UNITS, default='', null=True, max_length=255)

    def __str__(self):
        return self.name
