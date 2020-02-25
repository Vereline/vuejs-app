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
        title = graphene.String()
        full_text = graphene.String()
        author = graphene.Int()
        # image = graphene.String()

    def mutate(self, info, title, full_text, author):
        blog_post = BlogPost(title=title, full_text=full_text, author_id=author)
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

    def mutate(self, info, id, title, full_text):
        blog_post = BlogPost.objects.get(pk=id)
        blog_post.title = title
        blog_post.full_text = full_text
        blog_post.save()
        ok = True
        return UpdateBlogPost(blog_post=blog_post, ok=ok)


class BlogQuery(graphene.ObjectType):
    blog_posts = graphene.List(BlogPostType)

    def resolve_blog_posts(self, info):
        return BlogPost.objects.all()


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class CreateComment(graphene.Mutation):
    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentType)

    class Arguments:
        blog_post = graphene.String()
        author = graphene.String()
        text = graphene.String()

    def mutate(self, info, blog_post, author, text):
        comment = Comment(blog_post_id=blog_post, author_id=author, text=text)
        comment.save()
        ok = True
        return CreateComment(comment=comment, ok=ok)


class UpdateComment(graphene.Mutation):
    comment = graphene.Field(lambda: CommentType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()
        text = graphene.String()

    def mutate(self, info, id, text):
        comment = Comment.objects.get(pk=id)
        comment.text = text
        comment.save()
        ok = True
        return UpdateComment(comment=comment, ok=ok)


class CommentQuery(graphene.ObjectType):
    comments = graphene.List(CommentType)

    def resolve_comments(self, info):
        return Comment.objects.all()


class Mutations(graphene.ObjectType):
    create_blog_post = CreateBlogPost.Field()
    update_blog_post = UpdateBlogPost.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
