from rest_framework import serializers

from accounts.serializers import AuthorSerializer

from blogs.models import BlogPost, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'blog_post',
            'author',
            'text',
        )


class ModifyCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'blog_post',
            'author',
            'text',
        )


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = BlogPost
        fields = (
            'id',
            'title',
            'full_text',
            'author',
            'image',
            'comments',
        )


class ModifyBlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = (
            'id',
            'title',
            'full_text',
            'author',
            'image',
        )
