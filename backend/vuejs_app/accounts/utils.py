import datetime
import logging


logger = logging.getLogger(__name__)


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        logger.error("Incorrect date format, should be YYYY-MM-DD")
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

