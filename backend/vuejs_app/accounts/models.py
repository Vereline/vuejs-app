import datetime
import logging
import os
import re
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete

from vuejs_app.settings import STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL


logger = logging.getLogger(__name__)
# Create your models here.

default_image_path = '{0}/images/user-default.png'.format(STATICFILES_DIRS[0])


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location='{0}/'.format(MEDIA_ROOT),
    # Url for file
    base_url=MEDIA_URL,
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatars/<filename>
    new_filename = instance.create_photo_name(instance.username) + '.' + filename.split('.')[-1]
    return 'avatars/{0}'.format(new_filename)


class User(AbstractUser):
    photo = models.ImageField(upload_to=image_directory_path, storage=image_storage, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, update_photo=False, *args, **kwargs):
        """ Save User model."""
        try:
            if not self.photo:
                # set default picture
                default_image = open(default_image_path, 'rb')
                self.photo = image_storage.save(image_directory_path(self, default_image_path), default_image)
                default_image.close()
                logging.info('Create unique file name: ' + self.photo.name)

            elif update_photo:
                file_name = self.photo.name.split('.')
                new_file_name = self.create_photo_name(self.username)

                # Rename image file into unique value
                self.photo.name = new_file_name + '.' + file_name[-1]
                logging.info('Create unique file name: ' + new_file_name)

        except Exception as ex:
            logger.error("Error trying to save model: saving image failed: " + repr(ex))

        super(User, self).save(*args, **kwargs)

    @staticmethod
    def create_photo_name(username):
        date_string = datetime.datetime.now().strftime("%m-%d-%Y")
        return '{0}_{1}'.format(username, date_string)


def delete_unused_photos(sender, instance, **kwargs):
    """
    Deletes all User photos for all the time of using Vickytrip-api
    :param sender:
    :param instance: User object
    :param kwargs:
    :return:
    """
    logger.info('Delete {}'.format(instance.photo.name))
    try:
        storage, path = instance.photo.storage, instance.photo.path
        storage.delete(path)
        user_name = instance.username
        photo_name_regex = re.compile(user_name + '_\d{2}-\d{2}-\d{4}(_+(.)*)?\\.(png|jpg|jpeg|bmp|gif)')
        photo_storage = storage.location + '/avatars/'
        all_files = os.listdir(photo_storage)
        for filename in all_files:
            if photo_name_regex.match(filename):
                try:
                    os.remove(photo_storage + filename)
                except Exception as ex:
                    logger.error(ex)
                else:
                    logger.info('Successful deleting {}'.format(filename))
    except Exception as ex:
        logger.error(ex)
    else:
        logger.info('Successful deleting files of user {}'.format(user_name))


pre_delete.connect(delete_unused_photos, sender=User)
