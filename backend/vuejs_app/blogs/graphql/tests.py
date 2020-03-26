from django.urls import reverse
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase

from accounts.models import User
from blogs.models import BlogPost, Comment
from vuejs_app.schema import schema


class TestGraphqlSchemaBlogPost(GraphQLTestCase):
    """
    Tests for all blog graphql queries and mutations
    """
    # URL to graphql endpoint
    GRAPHQL_URL = reverse('graphql-view')
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        cls.admin_test_username = 'adminTestUser'
        cls.admin_test_email = 'admintest@user.com'
        cls.admin_test_password = 'admin12345678'
        admin_user = User.objects.create(username=cls.admin_test_username, email=cls.admin_test_email,
                                         password=cls.admin_test_password, is_active=True, is_staff=True)
        admin_user.set_password(cls.admin_test_password)
        admin_user.save()
        cls.blog = BlogPost.objects.create(title='TestTitle', full_text='Full text', author=admin_user)
        cls.blog_test_data = {
            'full_text': 'Updated blog text',
            'title': 'Title',
            'author': admin_user.id
        }

    def test_get_blog_posts(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute('''
        query allBlogPosts {
            blogPosts {
                id,
                title,
                fullText,
                author {
                    id,
                    firstName,
                    lastName
                },
                createdAt,
                updatedAt
            }
        }
        ''')
        blog_count = BlogPost.objects.count()
        self.assertEqual(len(response['data']['blogPosts']), blog_count)

    def test_get_blog_post(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute('''
        query blogPostQuery($id: Int!) {
            blogPost(id: $id) {
                id,
                title,
                fullText,
                image,
                author {
                    id,
                    firstName,
                    lastName,
                    photo
                },
                createdAt,
                updatedAt,
                comments {
                    id,
                    text,
                    createdAt,
                    updatedAt,
                    author {
                       id,
                        firstName,
                        lastName,
                       photo
                    },
                }
            }
        }
        ''')
        self.assertEqual(response['data']['blogPost']['id'], self.blog.id)

    def test_create_blog_posts(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
            mutation createBlog($title:String!, $fullText: String!, $authorId: Int!) {
                createBlogPost(title: $title, fullText: $fullText, authorId: $authorId) {
                    blogPost {
                        title
                        fullText
                        author {
                          id
                        }
                    }
                    ok
                }
            }
        ''',
            variable_values=self.blog_test_data
        )
        self.assertEqual(response['data']['createBlogPost']['blogPost']['title'], self.blog_test_data['title'])

    def test_update_blog_posts(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
            mutation updateBlog($title:String!, $fullText: String!, $id: String!) {
                  updateBlogPost(title: $title, fullText: $fullText, id: $id) {
                    blogPost {
                      id
                      title
                      fullText
                    }
                    ok
                }
            }
            ''',
            variable_values=self.blog_test_data
        )
        self.assertEqual(response['data']['createBlogPost']['blogPost']['title'], self.blog_test_data['title'])


class TestGraphqlSchemaComment(GraphQLTestCase):
    """
    Tests for all comments graphql queries and mutations
    """
    # URL to graphql endpoint
    GRAPHQL_URL = reverse('graphql-view')
    # test case's schema
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUp(cls):
        cls.admin_test_username = 'adminTestUser'
        cls.admin_test_email = 'admintest@user.com'
        cls.admin_test_password = 'admin12345678'
        admin_user = User.objects.create(username=cls.admin_test_username, email=cls.admin_test_email,
                                         password=cls.admin_test_password, is_active=True, is_staff=True)
        admin_user.set_password(cls.admin_test_password)
        admin_user.save()
        cls.blog = BlogPost.objects.create(title='TestTitle', full_text='Full text', author=admin_user)
        cls.comment = Comment.objects.create(text='Comment text', blog_post=cls.blog, author=admin_user)
        cls.comment_test_data = {
            'text': 'Updated text',
            'blog_post': cls.blog.id,
            'author': admin_user.id
        }

    def test_get_comment(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''

        ''')
        self.assertEqual(response['data']['comment']['id'], self.comment.id)

    def test_get_comments(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
        ''')
        comments_count = Comment.objects.count()
        self.assertEqual(len(response['data']['comments']), comments_count)

    def test_update_comment(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
            mutation updateComment($text: String!, $id: String!) {
                updateComment(text: $text, id: $id) {
                    ok
                    comment {
                        id
                        text
                        author {
                            id
                            firstName,
                            lastName
                        }
                        blogPost {
                            id
                        }
                    }
                }
            }
        ''',
            variable_values=self.comment_test_data
        )
        self.assertEqual(response['data']['updateComment']['comment']['text'], self.comment_test_data['text'])

    def test_create_comment(self):
        client = Client(self.GRAPHQL_SCHEMA)
        response = client.execute(
            '''
            mutation addComment($text: String!, $blogPostId: String!, $authorId: String!) {
                createComment(text: $text, blogPost: $blogPostId, author: $authorId) {
                    ok
                    comment {
                        id
                        text
                        author {
                            id
                            firstName,
                            lastName
                        }
                        blogPost {
                            id
                        }
                    }
                }
            }
        ''',
            variable_values=self.comment_test_data
        )
        self.assertEqual(response['data']['createComment']['comment']['text'], self.comment_test_data['text'])
