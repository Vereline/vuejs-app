from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    """
    Special empty view which will check if person is authenticated or not
    """
    pass
