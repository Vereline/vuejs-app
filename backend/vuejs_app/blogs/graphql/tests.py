import json

from graphene_django.utils.testing import GraphQLTestCase
from vuejs_app.schema import schema


class TestGraphqlSchemaBlogPost(GraphQLTestCase):
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        pass
    # mutation createBlog($title:String!, $fullText: String!, $authorId: Int!) {
    #       createBlogPost(title: $title, fullText: $fullText, authorId: $authorId) {
    #         blogPost {
    #             title
    #             fullText
    #           	author {
    #           	  id
    #           	}
    #         }
    #         ok
    #     }
    # }

    # mutation updateBlog($title:String!, $fullText: String!, $id: String!) {
    #       updateBlogPost(title: $title, fullText: $fullText, id: $id) {
    #         blogPost {
    #           id
    #           title
    #           fullText
    #         }
    #         ok
    #     }
    # }

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
        # mutation updateComment($text: String!, $id: String!) {
        #   updateComment(text: $text, id: $id) {
        #     ok
        #     comment{
        #       id
        #       text
        #       author {
        #         id
        #         firstName,
        #         lastName
        #       }
        #       blogPost {
        #         id
        #       }
        #     }
        #   }
        # }

        # mutation addComment($text: String!, $blogPostId: String!, $authorId: String!) {
        #   createComment(text: $text, blogPost: $blogPostId, author: $authorId) {
        #     ok
        #     comment{
        #       id
        #       text
        #       author {
        #         id
        #         firstName,
        #         lastName
        #       }
        #       blogPost {
        #         id
        #       }
        #     }
        #   }
        # }
        pass

    def test_schema(self):
        pass
