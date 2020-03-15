import json

from graphene_django.utils.testing import GraphQLTestCase
from vuejs_app.schema import schema


class TestGraphqlSchemaUser(GraphQLTestCase):
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        pass

    def test_some_query(self):
        response = self.query(
            '''
            query {
                myModel {
                    id
                    name
                }
            }
            ''',
            op_name='myModel'
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
