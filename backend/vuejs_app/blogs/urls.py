from django.urls import path

from blogs.views import BlogPostView, CommentView

urlpatterns = [
    path('blog-posts/<int:blog_id>/comments/<int:pk>/',
         CommentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment-detail'),
    path('blog-posts/<int:blog_id>/comments/', CommentView.as_view({'get': 'list', 'post': 'create'}), name='comments'),
    path('blog-posts/<int:pk>/', BlogPostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='blog-post-detail'),
    path('blog-posts/', BlogPostView.as_view({'get': 'list', 'post': 'create'}), name='blog-posts'),
]
