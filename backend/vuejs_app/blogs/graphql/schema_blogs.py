import imghdr

import graphene
from django_graphene_permissions import permissions_checker
from django_graphene_permissions import PermissionDjangoObjectType
# from graphene_django.types import DjangoObjectType
# from graphene_permissions.mixins import AuthNode
# from graphene_permissions.permissions import AllowAuthenticated, AllowStaff
from default.graphql.schema import UploadMutation
from default.permissions import IsAdminOrReadOnlyGraphQL, IsAuthenticatedGraphQL

from ..models import BlogPost


class BlogPostType(PermissionDjangoObjectType):
    class Meta:
        model = BlogPost

    @staticmethod
    def permission_classes():
        return [IsAdminOrReadOnlyGraphQL]


class CreateBlogPost(graphene.Mutation):
    ok = graphene.Boolean()
    blog_post = graphene.Field(lambda: BlogPostType)

    class Arguments:
        title = graphene.String()
        full_text = graphene.String()
        author_id = graphene.Int()
        # image = graphene.String()

    @permissions_checker([IsAdminOrReadOnlyGraphQL])
    def mutate(self, info, title, full_text, author_id):
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        blog_post = BlogPost(title=title, full_text=full_text, author_id=author_id)
        blog_post.save()
        ok = True
        return CreateBlogPost(blog_post=blog_post, ok=ok)


class UpdateBlogPost(graphene.Mutation):
    blog_post = graphene.Field(lambda: BlogPostType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        title = graphene.String()
        full_text = graphene.String()

    @permissions_checker([IsAdminOrReadOnlyGraphQL])
    def mutate(self, info, id, title, full_text):
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.title = title
        blog_post.full_text = full_text
        blog_post.save()
        ok = True
        return UpdateBlogPost(blog_post=blog_post, ok=ok)


class BlogQuery(graphene.ObjectType):
    blog_post = graphene.Field(BlogPostType, id=graphene.Int())
    blog_posts = graphene.List(BlogPostType)

    @permissions_checker([IsAdminOrReadOnlyGraphQL])
    def resolve_blog_posts(self, info):
        # context will reference to the Django request
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        return BlogPost.objects.all()

    @permissions_checker([IsAdminOrReadOnlyGraphQL])
    def resolve_blog_post(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        id = kwargs.get('id')
        if id is not None:
            return BlogPost.objects.get(pk=id)
        return None


class UploadBlogImage(UploadMutation):

    def mutate(self, info, id, file, **kwargs):
        available_formats = ['png', 'jpg', 'jpeg', 'bmp', 'gif']
        if imghdr.what(file) not in available_formats:
            return UploadBlogImage(success=False)
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.image = file
        blog_post.save()
        return UploadBlogImage(success=True)


class Mutations(graphene.ObjectType):
    create_blog_post = CreateBlogPost.Field()
    update_blog_post = UpdateBlogPost.Field()
    upload_blog_image = UploadBlogImage.Field()
