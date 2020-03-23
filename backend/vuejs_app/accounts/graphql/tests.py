import json

from graphene_django.utils.testing import GraphQLTestCase

from accounts.models import User
from vuejs_app.schema import schema


class TestGraphqlSchemaUser(GraphQLTestCase):
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        cls.test_username = 'TestUser'
        cls.test_email = 'test@user.com'
        cls.test_password = '12345678'
        user = User.objects.create(username=cls.test_username, email=cls.test_email,
                                   password=cls.test_password, is_active=True)
        user.set_password(cls.test_password)
        user.save()

    def test_get_user(self):
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
            op_name='User'
        )
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
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        users_count = User.objects.count()
        self.assertEqual(len(content['data']['users']), users_count)

    def test_create_user(self):
        pass

    def test_update_user(self):
        pass
