from graphene import ObjectType, Schema
import accounts.graphql.schema as accounts_schema
import blogs.schema as blog_schema


class Query(accounts_schema.Query, blog_schema.BlogQuery, blog_schema.CommentQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(accounts_schema.UserMutation, blog_schema.Mutations, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)
