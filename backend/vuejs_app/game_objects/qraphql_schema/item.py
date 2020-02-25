import graphene
from graphene_django.types import DjangoObjectType
from game_objects.models import Item
# Create your views here.


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class CreateItem(graphene.Mutation):
    ok = graphene.Boolean()
    item = graphene.Field(lambda: ItemType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        item = Item(name=name)
        item.save()
        ok = True
        return CreateItem(item=item, ok=ok)


class UpdateItem(graphene.Mutation):
    item = graphene.Field(lambda: ItemType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        name = graphene.String()

    def mutate(self, info, id, name):
        item = Item.objects.get(pk=id)
        item.name = name
        item.save()
        ok = True
        return UpdateItem(item=item, ok=ok)


class ItemQuery(graphene.ObjectType):
    items = graphene.List(ItemType)

    def resolve_items(self, info):
        return Item.objects.all()


class Mutations(graphene.ObjectType):
    create_item = CreateItem.Field()
    update_item = UpdateItem.Field()
