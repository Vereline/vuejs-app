from rest_framework import permissions
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from blogs.models import BlogPost, Comment
from blogs.serializers import BlogPostSerializer, CommentSerializer
from blogs.utils import BlogPostSetPagination
# Create your views here.


class BlogPostView(ModelViewSet):
    """
    View to watch all BlogPosts, also to create/update/delete BlogPost objects
    create: Create new blog post
    update: Update existing blog post
    destroy: Delete blog post
    list: Get list of blog posts
    retrieve: Get 1 blog post with id
    """
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostSetPagination
    permission_classes = (IsAuthenticated, )
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    parser_classes = (JSONParser, MultiPartParser, )
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.queryset
        else:
            return self.queryset.filter(author=self.request.user)


class CommentView(ModelViewSet):
    """
    View to watch all Comments, also to create/update/delete Comment objects
    create: Create new comments message
    update: Update existing comment
    destroy: Delete comment
    list: Get list of comments
    retrieve: Get 1 comment with id
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    parser_classes = (JSONParser, )
    queryset = Comment.objects.all()

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id', None)
        if not blog_id:
            return self.queryset
        else:
            return self.queryset.filter(blog_post_id=blog_id)
