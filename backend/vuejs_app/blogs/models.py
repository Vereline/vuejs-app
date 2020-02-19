import datetime
import logging
import os
import re

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_delete

from accounts.models import User
from blogs.managers import BlogPostManager, CommentManager
from default.models import TimestampedModel


logger = logging.getLogger(__name__)
# Create your models here.


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location='{0}/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=settings.MEDIA_URL,
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/blog_images/<filename>
    new_filename = instance.create_image_name(instance.author.username) + '.' + filename.split('.')[-1]
    return 'blog_images/{0}'.format(new_filename)


class BlogPost(TimestampedModel):
    """
    Personal blog post model
    """
    title = models.CharField(default='', max_length=255, null=False)
    full_text = models.TextField(default='', null=False)
    author = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path, storage=image_storage, blank=True, null=True)

    objects = BlogPostManager()

    def __str__(self):
        return 'BlogPost #{0}'.format(self.id)

    @staticmethod
    def create_image_name(author_username):
        date_string = datetime.datetime.now().strftime("%m-%d-%Y")
        return '{0}_{1}'.format(author_username, date_string)


class Comment(TimestampedModel):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    text = models.CharField(default='', max_length=255, null=True)

    objects = CommentManager()

    def __str__(self):
        return 'Comment #{0}'.format(self.id)


def delete_unused_images(sender, instance, **kwargs):
    """
    Deletes all User photos for all the time of using Vickytrip-api
    :param sender:
    :param instance: BlogPost object
    :param kwargs:
    :return:
    """        
    logger.info('Delete {}'.format(instance.image.name))
    try:
        storage, path = instance.image.storage, instance.image.path
        storage.delete(path)
        blog_post_pk = instance.pk
        image_name_regex = re.compile(blog_post_pk + '_\d{2}-\d{2}-\d{4}(_+(.)*)?\\.(png|jpg|jpeg|bmp|gif)')
        im_storage = storage.location + '/news_images/'
        all_files = os.listdir(im_storage)
        for filename in all_files:
            if image_name_regex.match(filename):
                try:
                    os.remove(im_storage + filename)
                except Exception as ex:
                    logger.error(ex)
                else:
                    logger.info('Successful deleting {}'.format(filename))
    except Exception as ex:
        logger.error(ex)
    else:
        logger.info('Successful deleting files of BlogPost {}'.format(blog_post_pk))


pre_delete.connect(delete_unused_images, sender=BlogPost)
