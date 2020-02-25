import graphene
from graphene_django.types import DjangoObjectType
from game_objects.models import Place
# Create your views here.


class PlaceType(DjangoObjectType):
    class Meta:
        model = Place


class CreatePlace(graphene.Mutation):
    ok = graphene.Boolean()
    place = graphene.Field(lambda: PlaceType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        place = Place(name=name)
        place.save()
        ok = True
        return CreatePlace(place=place, ok=ok)


class UpdatePlace(graphene.Mutation):
    place = graphene.Field(lambda: PlaceType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        name = graphene.String()

    def mutate(self, info, id, name):
        place = Place.objects.get(pk=id)
        place.name = name
        place.save()
        ok = True
        return UpdatePlace(place=place, ok=ok)


class PlaceQuery(graphene.ObjectType):
    places = graphene.List(PlaceType)

    def resolve_places(self, info):
        return Place.objects.all()


class Mutations(graphene.ObjectType):
    create_place = CreatePlace.Field()
    update_place = UpdatePlace.Field()
