import json

from django.urls import reverse
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from graphql_jwt.testcases import JSONWebTokenTestCase
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User
from vuejs_app.schema import schema


class TestGraphqlSchemaUser(GraphQLTestCase):
    """

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
        cls.create_input = '''
        {
            "input": {
                "firstName": "Asd",
                "lastName": "Asd",
                "username": "AsdAsd",
                "password": "12345678",
                "email": "Asd@asd.asd"
            }
        }
        '''
        cls.update_input = '''
        {
            "id": 1,
            "input": {
                  "firstName": "Asd",
                  "lastName": "Asd",
                  "username": "AsdAsd",
                  "email": "Asd@asd.asd"
            }
        }
        '''
        # cls.client = Client(schema)

    def setUpClient(self):
        client = APIClient()
        login_response = client.post('/accounts/token-auth/',
                                     {
                                         'username_or_email': self.test_username,
                                         'password': self.test_password
                                     }
                                     )
        # client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['token'])
        # return client
        return login_response.data['token']

    def test_get_user(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = self.query(
            '''
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
            ''',
            op_name='User',
            headers={
                'Authorization': 'Bearer ' + self.setUpClient()
            }
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertEqual(content['data']['user']['id'], 1)

    def test_get_users(self):
        response = self.query(
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
            ''',
            op_name='User'
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        users_count = User.objects.count()
        self.assertEqual(len(content['data']['users']), users_count)

    def test_create_user(self):
        response = self.query(
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
            op_name='User',
            input_data=self.create_input
        )
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        users_count = User.objects.count()
        self.assertEqual(len(content['data']['users']), users_count)

    def test_update_user(self):
        response = self.query(
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
            op_name='User',
            input_data=self.update_input
        )
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        users_count = User.objects.count()
        self.assertEqual(len(content['data']['users']), users_count)


class TestGraphqlAuthentication(JSONWebTokenTestCase):
    """

    """
    # URL to graphql endpoint
    GRAPHQL_URL = reverse('graphql-view')
    GRAPHQL_SCHEMA = schema

    auth_mutation = '''
        mutation TokenAuth($username: String!, $password: String!) {
          tokenAuth(username: $username, password: $password) {
            token
            payload
            refreshExpiresIn
          }
    }
    '''

    verify_token = '''
        mutation VerifyToken($token: String!) {
          verifyToken(token: $token) {
            payload
          }
        }
    '''

    refresh_token = '''
        mutation RefreshToken($token: String!) {
          refreshToken(token: $token) {
            token
            payload
            refreshExpiresIn
          }
        }
    '''

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.client.authenticate(self.user)

    def test_get_user(self):
        query = '''
        query GetUser($username: String!) {
          user(username: $username) {
            id
          }
        }'''

        variables = {
          'username': self.user.username,
        }

        self.client.execute(query, variables)
