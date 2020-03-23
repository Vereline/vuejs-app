import json

from graphene_django.utils.testing import GraphQLTestCase
from vuejs_app.schema import schema


class TestGraphqlSchemaUser(GraphQLTestCase):
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        pass

    def test_get_user(self):
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

    def test_get_users(self):
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

    def test_create_user(self):
        pass

    def test_update_user(self):
        pass
