from django.db import models
from default.utils import time_at_timezone
# Create your models here.


class TimestampedModel(models.Model):
    """
    Default base model. Contains time fields that allow to track object create/update/delete actions time.
    `deleted_at` is intended to be used instead of actually deleting the objects, so children models also require the
    custom Manager in order to filter out the deleted objects.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def local_created_at(self, timezone):
        return time_at_timezone(self.created_at, timezone)

    def local_updated_at(self, timezone):
        return time_at_timezone(self.updated_at, timezone)

    @property
    def is_deleted(self):
        return self.deleted_at is not None
