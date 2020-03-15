from graphene import ObjectType, Schema
# from graphene_django.debug import DjangoDebug

import accounts.graphql.schema as accounts_schema
import blogs.graphql.schema as blog_schema


class Query(accounts_schema.Query, blog_schema.BlogQuery, blog_schema.CommentQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project

    # field for debugging graphql queries
    # debug = graphene.Field(DjangoDebug, name='_debug')

    pass


class Mutation(accounts_schema.UserMutation, blog_schema.Mutations, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)
