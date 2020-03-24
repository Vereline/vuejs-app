from graphene import ObjectType, Schema, Field
# from graphql_jwt import ObtainJSONWebToken, Verify, Refresh, Revoke
from graphene_django.debug import DjangoDebug

import accounts.graphql.schema as accounts_schema
import blogs.graphql.schema_comments as comments_schema
import blogs.graphql.schema_blogs as blog_schema


class Query(
    accounts_schema.Query,
    blog_schema.BlogQuery,
    comments_schema.CommentQuery,
    ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project

    # field for debugging graphql queries
    debug = Field(DjangoDebug, name='_debug')


class Mutation(
    accounts_schema.UserMutation,
    comments_schema.Mutations,
    blog_schema.Mutations, ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    # token_auth = ObtainJSONWebToken.Field()
    # verify_token = Verify.Field()
    # refresh_token = Refresh.Field()
    # revoke_token = Revoke.Field()
    pass


schema = Schema(query=Query, mutation=Mutation)
