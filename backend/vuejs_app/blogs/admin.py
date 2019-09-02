from django.contrib import admin
from django.utils.safestring import mark_safe

from blogs.models import BlogPost, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    fields = (
        'blog_post',
        'author',
        'text',
    )


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = (
        '__str__',
        'title',
        'author',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'title',
        'full_text',
        'author',
        'image',
        'upload_image',
    )
    inlines = [
        CommentInline,
    ]
    readonly_fields = ('upload_image',)

    def upload_image(self, obj):
        if obj.image:
            width = obj.image.width if obj.image.width < 300 else 300
            height = obj.image.height / (obj.image.width / width)
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=width,
                height=height,
                )
            )
        else:
            return mark_safe('<p>No title image</p>')


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = (
        '__str__',
        'blog_post',
        'author',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    fields = (
        'blog_post',
        'author',
        'text',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
