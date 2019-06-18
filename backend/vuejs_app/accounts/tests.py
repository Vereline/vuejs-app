from django.test import TestCase
from accounts.models import User
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status
# Create your tests here.


class TestJWTAuthentication(TestCase):

    @classmethod
    def setUpTestData(cls):
        # set up test database
        cls.test_username = 'TestUser'
        cls.test_email = 'test@user.com'
        cls.test_password = '12345678'
        user = User.objects.create(username=cls.test_username, email=cls.test_email,
                                   password=cls.test_password, is_active=True)
        user.set_password(cls.test_password)
        user.save()
        cls.test_data = {
            'username': 'user_name',
            'email': 'email@mail.com',
            'password': 'Password',
            'first_name': 'First',
            'last_name': 'Last',
            'birth_date': '2012-12-12',
        }
        cls.update_test_data = {
            'email': 'email@mail.com',
            'first_name': 'First',
            'last_name': 'Last',
        }
        cls.factory = APIRequestFactory()

    def test_refresh_token(self):
        client = APIClient()
        login_response = client.post('/accounts/token-auth/',
                                     {'username_or_email': self.test_username, 'password': self.test_password})
        self.assertTrue('token' in login_response.data.keys())
        token = login_response.data['token']
        client.credentials(Authorisation='Bearer ' + token)
        refresh_response = client.post('/accounts/token-refresh/', {'token': token})
        self.assertTrue('token' in refresh_response.data.keys())
        self.assertTrue(refresh_response.status_code == status.HTTP_200_OK)

    def test_verify_token(self):
        client = APIClient()
        login_response = client.post('/accounts/token-auth/',
                                     {'username_or_email': self.test_username, 'password': self.test_password})
        self.assertTrue('token' in login_response.data.keys())
        token = login_response.data['token']
        client.credentials(Authorisation='Bearer ' + token)
        verify_response = client.post('/accounts/token-verify/', {'token': token})
        self.assertTrue('token' in verify_response.data.keys())
        self.assertTrue(verify_response.status_code == status.HTTP_200_OK)

    def test_auth_token(self):
        client = APIClient()
        response = client.post('/accounts/token-auth/',
                               {'username_or_email': self.test_username, 'password': self.test_password})
        self.assertTrue('token' in response.data)
        self.assertTrue(response.status_code == status.HTTP_200_OK)

    def test_user_creation(self):
        client = APIClient()
        response = client.post('/accounts/signup/', self.test_data)
        try:
            test_user = User.objects.get(username=self.test_data['username'])
        except User.DoesNotExist:
            test_user = None
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)
        self.assertIsNotNone(test_user)
        self.assertTrue('token' in response.data)

    def test_user_update(self):
        client = APIClient()
        client.login(username=self.test_username, password=self.test_password)
        response = client.post('/accounts/update/', self.update_test_data)
        try:
            test_user = User.objects.get(username=self.test_username)
        except User.DoesNotExist:
            test_user = None
        self.assertTrue(response.status_code == status.HTTP_201_CREATED)
        self.assertIsNotNone(test_user)
        self.assertEquals(test_user.email, self.update_test_data['email'])
        self.assertTrue('token' in response.data)

    @classmethod
    def tearDownTestData(cls):
        # drop test database
        pass
