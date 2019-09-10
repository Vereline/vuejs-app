import json

from django.test import TestCase

from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status

from accounts.models import User
from blogs.models import BlogPost, Comment


# Create your tests here.


class BaseBlogAPITestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # set up test database
        cls.test_username = 'TestUser'
        cls.test_email = 'test@user.com'
        cls.test_password = '12345678'
        user = User.objects.create(username=cls.test_username, email=cls.test_email,
                                   password=cls.test_password, is_active=True, is_staff=False)
        user.set_password(cls.test_password)
        user.save()
        cls.admin_test_username = 'adminTestUser'
        cls.admin_test_email = 'admintest@user.com'
        cls.admin_test_password = 'admin12345678'
        admin_user = User.objects.create(username=cls.admin_test_username, email=cls.admin_test_email,
                                         password=cls.admin_test_password, is_active=True, is_staff=True)
        admin_user.set_password(cls.admin_test_password)
        admin_user.save()
        cls.blog = BlogPost.objects.create(title='TestTitle', full_text='Full text', author=admin_user)
        cls.comment = Comment.objects.create(text='Comment text', blog_post=cls.blog, author=user)
        cls.blog_test_data = {
            'full_text': 'Updated blog text',
            'title': 'Title',
            'author': admin_user.id
        }
        cls.comment_test_data = {
            'text': 'Updated text',
            'blog_post': 1,
            'author': admin_user.id
        }

        cls.factory = APIRequestFactory()

    def setUpClient(self):
        client = APIClient()
        login_response = client.post('/accounts/token-auth/',
                                         {
                                             'username_or_email': self.test_username,
                                             'password': self.test_password
                                         }
                                         )
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['token'])
        return client

    def setUpAdminClient(self):
        admin_client = APIClient()
        admin_login_response = admin_client.post('/accounts/token-auth/',
                                               {
                                                   'username_or_email': self.admin_test_email,
                                                   'password': self.admin_test_password
                                               }
                                               )
        admin_client.credentials(HTTP_AUTHORIZATION='Bearer ' + admin_login_response.data['token'])
        return admin_client


class TestBlogPost(BaseBlogAPITestCase):

    def test_list_blog_posts(self):
        client = self.setUpClient()
        response = client.get('/blogs/blog-posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_blog_post(self):
        client = self.setUpClient()
        response = client.get('/blogs/blog-posts/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_blog_post_succeed_staff(self):
        admin_client = self.setUpAdminClient()
        response = admin_client.post('/blogs/blog-posts/', self.blog_test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_blog_post_failed_non_staff(self):
        client = self.setUpClient()
        response = client.post('/blogs/blog-posts/', self.blog_test_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_blog_post_succeed_staff(self):
        admin_client = self.setUpAdminClient()
        response = admin_client.put('/blogs/blog-posts/1/', self.blog_test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_blog_post_failed_non_staff(self):
        client = self.setUpClient()
        response = client.put('/blogs/blog-posts/1/', self.blog_test_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_blog_post_succeed_staff(self):
        admin_client = self.setUpAdminClient()
        response = admin_client.delete('/blogs/blog-posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_blog_post_failed_non_staff(self):
        client = self.setUpClient()
        response = client.delete('/blogs/blog-posts/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestComment(BaseBlogAPITestCase):

    def test_list_comments(self):
        client = self.setUpClient()
        response = client.get('/blogs/blog-posts/1/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_comments(self):
        client = self.setUpClient()
        response = client.get('/blogs/blog-posts/1/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment_succeed(self):
        client = self.setUpClient()
        response = client.post('/blogs/blog-posts/1/comments/', json.dumps(self.comment_test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_comment_succeed(self):
        client = self.setUpClient()
        response = client.put('/blogs/blog-posts/1/comments/1/', json.dumps(self.comment_test_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment_succeed(self):
        client = self.setUpClient()
        response = client.delete('/blogs/blog-posts/1/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestGraphqlSchemaBlogPost(TestCase):
    @classmethod
    def setUp(cls):
        pass

    def test_schema(self):
        pass


class TestGraphqlSchemaComment(TestCase):
    @classmethod
    def setUp(cls):
        pass

    def test_schema(self):
        pass
