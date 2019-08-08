from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from blogs.models import BlogPost, Comment
from blogs.serializers import BlogPostSerializer, CommentSerializer
from blogs.utils import BlogPostSetPagination
# Create your views here.


class BlogPostView(ModelViewSet):
    """
    View to watch all BlogPosts, also to create/update/delete BlogPost objects 
    """
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostSetPagination
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.queryset
        else:
            return self.queryset.filter(author=self.request.user)


class CommentView(ModelViewSet):
    """
    View to watch all Comments, also to create/update/delete Comment objects
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id', None)
        if not blog_id:
            return self.queryset
        else:
            return self.queryset.filter(blog_post_id=blog_id)
