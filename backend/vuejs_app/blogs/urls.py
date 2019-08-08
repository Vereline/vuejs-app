from django.urls import path

from blogs.views import BlogPostView, CommentView

urlpatterns = [
    path('blog-posts/<int:pk>/', BlogPostView.as_view({'get': 'retrieve', 'put': 'update'}), name='blog-post-detail'),
    path('blog-posts', BlogPostView.as_view({'get': 'list', 'post': 'create'}), name='blog-posts'),
    path('comments', CommentView.as_view({'get'}), name='comments'),
]
