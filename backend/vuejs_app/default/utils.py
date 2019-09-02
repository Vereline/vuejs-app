import pytz

from django.utils import timezone


def time_at_timezone(time, timezone_code):
    """
    Return time in the specified timezone
    :param time: datetime objects
    :param timezone_code: string timezone code
    :return: datetime
    """
    tz = pytz.timezone(timezone_code)
    return time.astimezone(tz)


def delete_object(obj):
    """
    Function that should be used for deleting a single object across the whole application.
    Check if object has `deleted_at`. Set `deleted_at` if exists, delete object otherwise
    :param obj: any Model object
    """
    if obj is None:
        return
    if hasattr(obj, 'deleted_at'):
        obj.deleted_at = timezone.now()
        obj.save(update_fields=['deleted_at'])
    else:
        obj.delete()


def delete_qs(qs):
    """
    Function that should be used for deleting the QuerySet of objects across the whole application.
    Check if QuerySet's model has `deleted_at`. Set `deleted_at` if exists, delete the QuerySet otherwise.
    :param qs: any Model's queryset
    """
    if hasattr(qs.model, 'deleted_at'):
        qs.update(deleted_at=timezone.now())
    else:
        qs.delete()
