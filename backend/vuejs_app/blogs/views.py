from rest_framework import permissions
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from blogs.models import BlogPost, Comment
from blogs.serializers import BlogPostSerializer, CommentSerializer, ModifyBlogPostSerializer, ModifyCommentSerializer
from blogs.utils import BlogPostSetPagination, IsAdminOrReadOnly
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
    permission_classes = (IsAdminOrReadOnly, )
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, )
    parser_classes = (JSONParser, MultiPartParser, )
    queryset = BlogPost.objects.all()

    def get_serializer_class(self):
        # need this check to avoid fails of drf docs
        if self.request and self.request.method in ['POST', 'PUT']:
            return ModifyBlogPostSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.queryset.prefetch_related('comments')
        else:
            return self.queryset.filter(author_id=self.request.user.id).prefetch_related('comments')


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

    def get_serializer_class(self):
        # need this check to avoid fails of drf docs
        if self.request and self.request.method in ['POST', 'PUT']:
            return ModifyCommentSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        if self.request.method in permissions.SAFE_METHODS:
            queryset = self.queryset
        else:
            queryset = self.queryset.filter(author_id=self.request.user.id)

        blog_id = self.kwargs.get('blog_id', None)
        if blog_id:
            return queryset.filter(blog_post_id=blog_id)
        return queryset
