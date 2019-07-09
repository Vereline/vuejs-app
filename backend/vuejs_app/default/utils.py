import pytz


def time_at_timezone(time, timezone):
    """
    Return time in the specified timezone
    :param time: datetime objects
    :param timezone: string timezone code
    :return: datetime
    """
    tz = pytz.timezone(timezone)
    return time.astimezone(tz)
