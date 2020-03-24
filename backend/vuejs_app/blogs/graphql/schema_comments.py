import graphene
# from django_graphene_permissions import permissions_checker
from graphene_django.types import DjangoObjectType
# from default.permissions import IsAdminOrReadOnlyGraphQL, IsAuthenticatedGraphQL
# from graphene_permissions.mixins import AuthNode
# from graphene_permissions.permissions import AllowAuthenticated, AllowStaff
from ..models import Comment


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
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
