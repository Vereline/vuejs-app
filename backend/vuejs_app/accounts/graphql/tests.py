from django.urls import reverse
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
# from graphql_jwt.testcases import JSONWebTokenTestCase
# from rest_framework import status

from accounts.models import User
from vuejs_app.schema import schema


class TestGraphqlSchemaUser(GraphQLTestCase):
    """
    Tests for all users graphql queries and mutations
    """
    # URL to graphql endpoint
    GRAPHQL_URL = reverse('graphql-view')
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        cls.test_username = 'TestUser'
        cls.test_email = 'test@user.com'
        cls.test_password = '12345678'
        cls.test_user = User.objects.create(username=cls.test_username, email=cls.test_email,
                                            password=cls.test_password, is_active=True)
        cls.test_user.set_password(cls.test_password)
        cls.test_user.save()
        cls.create_input = {
            'input': {
                'firstName': 'Asd',
                'lastName': 'Asd',
                'username': 'AsdAsd',
                'password': '12345678',
                'email': 'Asd@asd.asd'
            }
        }

        cls.update_input = {
            'id': 1,
            'input': {
                  'firstName': 'Asd',
                  'lastName': 'Asd',
                  'username': 'AsdAsd',
                  'email': 'Asd@asd.asd'
            }
        }

    def test_get_user(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute('''
            query {
                user(id: 1) {
                    id,
                    username,
                    firstName,
                    lastName,
                    birthDate,
                    isActive,
                    isStaff,
                    email,
                }
            }
            ''')
        self.assertEqual(response['data']['user']['id'], '1')

    def test_get_users(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
            query {
                users {
                    id,
                    username,
                    firstName,
                    lastName,
                    birthDate,
                    isActive,
                    isStaff,
                    email,
                }
            }
            '''
        )
        users_count = User.objects.count()
        self.assertEqual(len(response['data']['users']), users_count)

    def test_create_user(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
                mutation CreateUser($input: UserInput!){
                  createUser(input: $input) {
                    user {
                        id,
                        firstName,
                        lastName,
                        username,
                        isActive,
                        email,
                    }
                    ok 
                  }
                }
            ''',
            variable_values=self.create_input
        )
        self.assertEqual(response['data']['createUser']['user']['username'], 'AsdAsd')

    def test_update_user(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
                mutation UpdateUser($input: UserInput!, $id: Int!){
                  updateUser(input: $input, id: $id) {
                    user {
                        id,
                        firstName,
                        lastName,
                        username,
                        isActive,
                        email,
                    }
                    ok 
                  }
                }
            ''',
            variable_values=self.update_input
        )
        self.assertEqual(response['data']['updateUser']['user']['username'], 'AsdAsd')


# class TestGraphqlAuthentication(JSONWebTokenTestCase):
#     """
#
#     """
#     # URL to graphql endpoint
#     GRAPHQL_URL = reverse('graphql-view')
#     GRAPHQL_SCHEMA = schema
#
#     auth_mutation = '''
#         mutation TokenAuth($username: String!, $password: String!) {
#           tokenAuth(username: $username, password: $password) {
#             token
#             payload
#             refreshExpiresIn
#           }
#     }
#     '''
#
#     verify_token = '''
#         mutation VerifyToken($token: String!) {
#           verifyToken(token: $token) {
#             payload
#           }
#         }
#     '''
#
#     refresh_token = '''
#         mutation RefreshToken($token: String!) {
#           refreshToken(token: $token) {
#             token
#             payload
#             refreshExpiresIn
#           }
#         }
#     '''
#
#     def setUp(self):
#         self.user = User.objects.create(username='test')
#         self.client.authenticate(self.user)
#
#     def test_get_user(self):
#         query = '''
#         query GetUser($username: String!) {
#           user(username: $username) {
#             id
#           }
#         }'''
#
#         variables = {
#           'username': self.user.username,
#         }
#
#         self.client.execute(query, variables)
