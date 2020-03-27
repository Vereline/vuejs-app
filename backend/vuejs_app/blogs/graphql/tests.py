import json

from django.urls import reverse
from graphene_django.utils.testing import GraphQLTestCase
from urllib.parse import urlencode

from rest_framework import status
from rest_framework.test import APIClient

from blogs.models import BlogPost, Comment
from blogs.tests import BaseBlogAPITestCase
from vuejs_app.schema import schema


class BaseBlogGraphQLTestCase(GraphQLTestCase, BaseBlogAPITestCase):
    # URL to graphql endpoint
    blog_test_data = {}
    comment_test_data = {}
    GRAPHQL_URL = reverse('graphql-view')
    # test case's schema
    GRAPHQL_SCHEMA = schema

    def url_string(self, **url_params):
        string = self.GRAPHQL_URL
        if url_params:
            string += "?" + urlencode(url_params)

        return string

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.blog_test_data['fullText'] = 'Updated blog text'
        cls.blog_test_data['authorId'] = cls.blog_test_data['author']
        cls.comment_test_data['blogPostId'] = cls.comment_test_data['blog_post']
        cls.comment_test_data['authorId'] = cls.comment_test_data['author']


class TestGraphqlSchemaBlogPost(BaseBlogGraphQLTestCase):
    """
    Tests for all blog graphql queries and mutations
    """
    # URL to graphql endpoint
    GRAPHQL_URL = reverse('graphql-view')
    # test case's schema
    GRAPHQL_SCHEMA = schema

    def test_get_blog_posts(self):
        client = self.setUpClient()
        response = client.get(self.url_string(
            query='''
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
                '''
        ))
        blog_count = BlogPost.objects.count()
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['blogPosts']), blog_count)

    def test_get_blog_post(self):
        client = self.setUpClient()
        response = client.get(self.url_string(
            query='''
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
            ''',
            variables=json.dumps({'id': self.blog.id})
        ))
        content = json.loads(response.content)
        self.assertEqual(content['data']['blogPost']['id'], str(self.blog.id))

    def test_create_blog_post(self):
        client = self.setUpAdminClient()
        response = client.post(self.url_string(
            query='''
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
            variables=json.dumps(self.blog_test_data)
        ))
        content = json.loads(response.content)
        self.assertEqual(content['data']['createBlogPost']['blogPost']['title'], self.blog_test_data['title'])

    def test_update_blog_posts(self):
        self.blog_test_data['id'] = self.blog.id
        client = self.setUpAdminClient()
        response = client.post(self.url_string(
            query='''
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
            variables=json.dumps(self.blog_test_data)
        ))
        content = json.loads(response.content)
        self.assertEqual(content['data']['updateBlogPost']['blogPost']['title'], self.blog_test_data['title'])

    def test_failed_to_get_blog_no_auth(self):
        client = APIClient()
        response = client.get(self.url_string(
            query='''
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
                '''
        ))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_fail_create_not_admin(self):
        client = self.setUpClient()
        response = client.post(self.url_string(
            query='''
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
            variables=json.dumps(self.blog_test_data)
        ))
        content = json.loads(response.content)
        self.assertEqual(content['errors'][0]['message'], 'Permission Denied.')
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestGraphqlSchemaComment(BaseBlogGraphQLTestCase):
    """
    Tests for all comments graphql queries and mutations
    """

    def test_get_comments(self):
        client = self.setUpClient()
        response = client.get(self.url_string(
            query='''
                query getComments {
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
            '''
        ))
        comments_count = Comment.objects.count()
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['comments']), comments_count)

    def test_get_comment(self):
        client = self.setUpClient()
        response = client.get(
            self.url_string(
                query='''
                    query getComment($id: Int!) {
                        comment(id: $id) {
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
                ''',
                variables=json.dumps({'id': self.comment.id})
            ))
        content = json.loads(response.content)
        self.assertEqual(content['data']['comment']['id'], str(self.comment.id))

    def test_update_comment(self):
        self.comment_test_data['id'] = self.comment.id
        client = self.setUpClient()
        response = client.post(
            self.url_string(
                query='''
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
                variables=json.dumps(self.comment_test_data)
            ))
        content = json.loads(response.content)
        self.assertEqual(content['data']['updateComment']['comment']['text'], self.comment_test_data['text'])

    def test_create_comment(self):
        client = self.setUpClient()
        response = client.post(
            self.url_string(
                query='''
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
                variables=json.dumps(self.comment_test_data)
            ))
        content = json.loads(response.content)
        self.assertEqual(content['data']['createComment']['comment']['text'], self.comment_test_data['text'])

    def test_failed_to_get_comment_no_auth(self):
        client = APIClient()
        response = client.get(self.url_string(
            query='''
                query getComments {
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
            '''
        ))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
