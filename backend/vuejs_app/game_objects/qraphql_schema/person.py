import graphene
from graphene_django.types import DjangoObjectType
from game_objects.models import Person
# Create your views here.


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class CreatePerson(graphene.Mutation):
    ok = graphene.Boolean()
    person = graphene.Field(lambda: PersonType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        person = Person(name=name)
        person.save()
        ok = True
        return CreatePerson(person=person, ok=ok)


class UpdatePerson(graphene.Mutation):
    person = graphene.Field(lambda: PersonType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        name = graphene.String()

    def mutate(self, info, id, name):
        person = Person.objects.get(pk=id)
        person.name = name
        person.save()
        ok = True
        return UpdatePerson(person=person, ok=ok)


class PersonQuery(graphene.ObjectType):
    persons = graphene.List(PersonType)

    def resolve_persons(self, info):
        return Person.objects.all()


class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
