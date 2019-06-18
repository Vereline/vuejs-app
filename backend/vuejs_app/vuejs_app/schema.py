from graphene import ObjectType, Schema
import accounts.schema


class Query(accounts.schema.Query, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(accounts.schema.UserMutation, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)
