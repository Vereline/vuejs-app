import json

from graphene_django.utils.testing import GraphQLTestCase
from vuejs_app.schema import schema


class TestGraphqlSchemaBlogPost(GraphQLTestCase):
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

        # Add some more asserts if you like
        ...

    def test_query_with_variables(self):
        response = self.query(
            '''
            query myModel($id: Int!){
                myModel(id: $id) {
                    id
                    name
                }
            }
            ''',
            op_name='myModel',
            variables={'id': 1}
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
        ...

    def test_some_mutation(self):
        response = self.query(
            '''
            mutation myMutation($input: MyMutationInput!) {
                myMutation(input: $input) {
                    my-model {
                        id
                        name
                    }
                }
            }
            ''',
            op_name='myMutation',
            input_data={'my_field': 'foo', 'other_field': 'bar'}
        )

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
        ...


class TestGraphqlSchemaComment(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        pass

    def test_schema(self):
        pass
