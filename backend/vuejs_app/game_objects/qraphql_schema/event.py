import graphene
from graphene_django.types import DjangoObjectType
from game_objects.models import Event, Ability
# Create your views here.


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class CreateEvent(graphene.Mutation):
    ok = graphene.Boolean()
    event = graphene.Field(lambda: EventType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        event = Event(name=name)
        event.save()
        ok = True
        return CreateEvent(event=event, ok=ok)


class UpdateEvent(graphene.Mutation):
    event = graphene.Field(lambda: EventType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        name = graphene.String()

    def mutate(self, info, id, name):
        event = Event.objects.get(pk=id)
        event.name = name
        event.save()
        ok = True
        return UpdateEvent(event=event, ok=ok)


class EventQuery(graphene.ObjectType):
    events = graphene.List(EventType)

    def resolve_events(self, info):
        return Event.objects.all()


class AbilityType(DjangoObjectType):
    class Meta:
        model = Ability


class CreateAbility(graphene.Mutation):
    ok = graphene.Boolean()
    ability = graphene.Field(lambda: AbilityType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        ability = Ability(name=name)
        ability.save()
        ok = True
        return CreateAbility(ability=ability, ok=ok)


class UpdateAbility(graphene.Mutation):
    ability = graphene.Field(lambda: AbilityType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        name = graphene.String()

    def mutate(self, info, id, name):
        ability = Ability.objects.get(pk=id)
        ability.name = name
        ability.save()
        ok = True
        return UpdateAbility(ability=ability, ok=ok)


class AbilityQuery(graphene.ObjectType):
    abilities = graphene.List(EventType)

    def resolve_abilities(self, info):
        return Ability.objects.all()


class Mutations(graphene.ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    create_ability = CreateAbility.Field()
    update_ability = UpdateAbility.Field()
