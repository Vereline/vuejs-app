from django.contrib import admin
from .models import Item, Place, Ability, Event, Person

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = (
        '__str__',
        'name',
        'type',
        'description',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'name',
        'type',
        'description',
        'weight',
        'price',
        'abilities',
    )


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = (
        '__str__',
        'name',
        'type',
        'description',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'name',
        'type',
        'description',
        'size',
        'flora',
        'fauna',
    )


class AbilityAdmin(admin.ModelAdmin):
    model = Ability
    list_display = (
        '__str__',
        'name',
        'type',
        'description',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'name',
        'type',
        'description',
        'persons',
        'power',
        'stamina_points',
    )


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = (
        '__str__',
        'name',
        'type',
        'description',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'name',
        'type',
        'description',
        'persons',
        'condition',
        'place',
        'items',
    )


class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = (
        '__str__',
        'name',
        'type',
        'description',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'name',
        'type',
        'description',
        'age',
        'first_name',
        'last_name',
        'race',
        'sex',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
