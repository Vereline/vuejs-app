from graphene import Field, List, ID, Int, InputObjectType, String, Mutation, Boolean
from graphene_django.types import DjangoObjectType, ObjectType
from accounts.models import User
from default.graphql.schema import UploadMutation
from default.permissions import IsAuthenticatedGraphQL


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
    first_name = String()
    last_name = String()
    password = String()
    email = String()


# Create mutations for users
class CreateUser(Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = Boolean()
    user = Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance = User(username=input.username, first_name=input.first_name, last_name=input.last_name,
                             password=input.password, is_active=True, email=input.email)
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
            user_instance.first_name = input.first_name
            user_instance.last_name = input.last_name
            user_instance.email = input.email
            user_instance.save()
            return UpdateUser(ok=ok, user=user_instance)
        return UpdateUser(ok=ok, user=None)

    @staticmethod
    def permission_classes():
        return [IsAuthenticatedGraphQL]


class UploadProfilePhoto(UploadMutation):

    def mutate(self, info, id, file, **kwargs):
        user = User.objects.get(pk=id)
        user.photo = file
        user.save()
        return UploadMutation(success=True)


class UserMutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    upload_profile_photo = UploadProfilePhoto.Field()
