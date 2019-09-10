from graphene import Field, List, ID, Int, InputObjectType, String, Mutation, Boolean
from graphene_django.types import DjangoObjectType, ObjectType
from accounts.models import User


# Create a GraphQL type for the User model
class UserType(DjangoObjectType):
    class Meta:
        model = User


# Create a Query type
class Query(ObjectType):
    user = Field(UserType, id=Int())
    users = List(UserType)

    def resolve_user(self, info, **kwargs):
        user_id = kwargs.get('id')

        if user_id is not None:
            return User.objects.get(pk=user_id)

        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


# Create Input Object Types
class UserInput(InputObjectType):
    id = ID()
    username = String()


# Create mutations for users
class CreateUser(Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = Boolean()
    user = Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance = User(username=input.username)
        user_instance.save()
        return CreateUser(ok=ok, user=user_instance)


class UpdateUser(Mutation):
    class Arguments:
        id = Int(required=True)
        input = UserInput(required=True)

    ok = Boolean()
    user = Field(UserType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        user_instance = User.objects.get(pk=id)
        if user_instance:
            ok = True
            user_instance.username = input.username
            user_instance.save()
            return UpdateUser(ok=ok, user=user_instance)
        return UpdateUser(ok=ok, user=None)


class UserMutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
