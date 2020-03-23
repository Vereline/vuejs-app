import graphene
from django_graphene_permissions import permissions_checker
from graphene_django.types import DjangoObjectType
from ..models import BlogPost, Comment
from default.permissions import IsAdminOrReadOnlyGraphQL, IsAuthenticatedGraphQL
# from graphene_permissions.mixins import AuthNode
# from graphene_permissions.permissions import AllowAuthenticated, AllowStaff


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost

    # @staticmethod
    # def permission_classes():
    #     return [IsAdminOrReadOnlyGraphQL]


class CreateBlogPost(graphene.Mutation):
    ok = graphene.Boolean()
    blog_post = graphene.Field(lambda: BlogPostType)

    class Arguments:
        title = graphene.String()
        full_text = graphene.String()
        author = graphene.Int()
        # image = graphene.String()

    def mutate(self, info, title, full_text, author):
        if not info.context.user.is_authenticated:
            # TODO: develop this stuff and create custom permission validators / decorators
            return BlogPost.objects.none()
        blog_post = BlogPost(title=title, full_text=full_text, author_id=author)
        blog_post.save()
        ok = True
        return CreateBlogPost(blog_post=blog_post, ok=ok)

    # @staticmethod
    # def permission_classes():
    #     return [IsAdminOrReadOnlyGraphQL]


class UpdateBlogPost(graphene.Mutation):
    blog_post = graphene.Field(lambda: BlogPostType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        title = graphene.String()
        full_text = graphene.String()

    def mutate(self, info, id, title, full_text):
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.title = title
        blog_post.full_text = full_text
        blog_post.save()
        ok = True
        return UpdateBlogPost(blog_post=blog_post, ok=ok)

    # @staticmethod
    # def permission_classes():
    #     return [IsAdminOrReadOnlyGraphQL]


class BlogQuery(graphene.ObjectType):
    blog_post = graphene.Field(BlogPostType, id=graphene.Int())
    blog_posts = graphene.List(BlogPostType)

    # @permissions_checker([IsAdminOrReadOnlyGraphQL])
    def resolve_blog_posts(self, info):
        # context will reference to the Django request
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        return BlogPost.objects.all()

    # @permissions_checker([IsAdminOrReadOnlyGraphQL])
    def resolve_blog_post(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return BlogPost.objects.none()
        id = kwargs.get('id')
        if id is not None:
            return BlogPost.objects.get(pk=id)
        return None

    # @staticmethod
    # def permission_classes():
    #     return [IsAdminOrReadOnlyGraphQL]


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

    # @staticmethod
    # def permission_classes():
    #     return [IsAuthenticatedGraphQL]


class CreateComment(graphene.Mutation):
    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    class Arguments:
        blog_post = graphene.String()
        author = graphene.String()
        text = graphene.String()

    def mutate(self, info, blog_post, author, text):
        if not info.context.user.is_authenticated:
            return Comment.objects.none()
        comment = Comment(blog_post_id=blog_post, author_id=author, text=text)
        comment.save()
        ok = True
        return CreateComment(comment=comment, ok=ok)

    # @staticmethod
    # def permission_classes():
    #     return [IsAuthenticatedGraphQL]


class UpdateComment(graphene.Mutation):
    comment = graphene.Field(lambda: CommentType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        text = graphene.String()

    def mutate(self, info, id, text):
        if not info.context.user.is_authenticated:
            return Comment.objects.none()
        comment = Comment.objects.get(pk=id)
        comment.text = text
        comment.save()
        ok = True
        return UpdateComment(comment=comment, ok=ok)

    # @staticmethod
    # def permission_classes():
    #     return [IsAuthenticatedGraphQL]


class CommentQuery(graphene.ObjectType):
    comment = graphene.Field(CommentType, id=graphene.Int())
    comments = graphene.List(CommentType)

    def resolve_comments(self, info):
        if not info.context.user.is_authenticated:
            return Comment.objects.none()
        return Comment.objects.all()

    def resolve_comment(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return Comment.objects.none()
        id = kwargs.get('id')
        if id is not None:
            return Comment.objects.get(pk=id)
        return None

    # @staticmethod
    # def permission_classes():
    #     return [IsAuthenticatedGraphQL]


class Mutations(graphene.ObjectType):
    create_blog_post = CreateBlogPost.Field()
    update_blog_post = UpdateBlogPost.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
