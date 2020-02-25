import graphene
from graphene_django.types import DjangoObjectType
from .models import BlogPost, Comment


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost


class CreateBlogPost(graphene.Mutation):
    ok = graphene.Boolean()
    blog_post = graphene.Field(lambda: BlogPostType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, description):
        blog_post = BlogPost(name=name, description=description, isDone=False)
        blog_post.save()
        ok = True
        return CreateBlogPost(blog_post=blog_post, ok=ok)


class UpdateBlogPost(graphene.Mutation):
    blog_post = graphene.Field(lambda: BlogPostType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        IsDone = graphene.Boolean()

    def mutate(self, info, id, IsDone):
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.isDone = IsDone
        blog_post.save()
        ok = True
        return UpdateBlogPost(blog_post=blog_post, ok=ok)


class BlogQuery(graphene.ObjectType):
    blog_posts = graphene.List(BlogPostType)

    def resolve_tasks(self, info):
        return BlogPost.objects.all()


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class CreateComment(graphene.Mutation):
    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, description):
        comment = Comment(name=name, description=description, isDone=False)
        comment.save()
        ok = True
        return CreateComment(comment=comment, ok=ok)


class UpdateComment(graphene.Mutation):
    comment = graphene.Field(lambda: CommentType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        IsDone = graphene.Boolean()

    def mutate(self, info, id, IsDone):
        comment = Comment.objects.get(pk=id)
        comment.isDone = IsDone
        comment.save()
        ok = True
        return UpdateComment(comment=comment, ok=ok)


class CommentQuery(graphene.ObjectType):
    comments = graphene.List(CommentType)

    def resolve_tasks(self, info):
        return Comment.objects.all()


class Mutations(graphene.ObjectType):
    create_blog_post = CreateBlogPost.Field()
    update_blog_post = UpdateBlogPost.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
