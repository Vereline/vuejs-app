from django.db import models


class BaseManager(models.Manager):
    def _get_base_queryset(self):
        return super().get_queryset()

    def get_queryset(self):
        return self._get_base_queryset().filter(deleted_at__isnull=True)

    def get_deleted(self):
        return self._get_base_queryset().filter(deleted_at__isnull=False)

    def get_all(self):
        return self._get_base_queryset()
